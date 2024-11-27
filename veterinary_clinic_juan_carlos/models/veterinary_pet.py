from odoo import models, fields, api
import random
import string
from odoo.exceptions import ValidationError


def generate_random_chip(lengk=12):
    caract = string.ascii_letters + string.digits
    return ''.join(random.choices(caract, k=lengk))

class VeterinaryPet(models.Model):
    _name = "veterinary.pet"
    _description = "Veterinary Pet"

    name = fields.Char(string="Name", required=True, help="Name of the pet", default="garritas")
    birthdate = fields.Date(string="Birthdate", help="Birthdate of the pet")
    weight = fields.Float(string="Weight")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    number_pet = fields.Char(string="Number Pet", copy=False)
    species_id = fields.Many2one('veterinary.animalspecies', string='Species', help='Species of the pet')
    # species = fields.Selection([
    #     ("cat", "Cat"),
    #     ("dog", "Dog"),
    #     ("other", "Other"),
    #     ("bird", "Bird"),
    # ])
    vaccinated = fields.Boolean(string="Vaccinated", compute="_compute_vaccinated", inverse="_inverse_vaccinated", store=True)
    last_vaccination_date = fields.Date(string="Last Vaccination Date")

    pet_image = fields.Image(string="Photo")
    allergy_ids = fields.Many2many("veterinary.allergy", string="Allergy")
    adopted = fields.Boolean(string="Adopted")
    
    appointment_ids = fields.One2many("veterinary.appointment", "pet_id")
    appointment_count = fields.Integer(compute="_compute_appointment_count")

    insurance_ids = fields.One2many("veterinary.insurance", "pet_id")
    insurance_count = fields.Integer(compute="_compute_insurance_count")

    active = fields.Boolean(string="Active", default=True)


    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = len(record.insurance_ids)

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def action_view_history(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Medical History",
            "res_model": "veterinary.appointment",
            "view_mode": "tree,form",
            "domain": [("pet_id", "=", self.id)]
        }

    def action_view_history_insurance(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Insurence History",
            "res_model": "veterinary.insurance",
            "view_mode": "tree,form",
            "domain": [("pet_id", "=", self.id)]
            # "domain": [("id", "in", self.insurance_ids.ids)]
        }

    def action_finish_surgeries(self):
        surgeries = self.env["veterinary.surgeries"].search([("pet_id", "=", self.id)])
        for surgerie in surgeries:
            surgerie.action_completed()

    def _inverse_vaccinated(self):
        for record in self:
            if record.vaccinated:
                record.last_vaccination_date = fields.Date.today()
            else:
                record.last_vaccination_date = False

    @api.depends("last_vaccination_date")
    def _compute_vaccinated(self):
        for record in self:
            record.vaccinated = bool(record.last_vaccination_date)
    
    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def action_chip_number_pet(self):
        for record in self:
            record.number_pet = generate_random_chip()

    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365
                # record.write ({"age : 0"})
                
    # def create_copy(self):
    #     self.copy({"name" : "copy of " + self.name})
                   
    def create_insurance(self):
        self.env["veterinary.insurance"].create({"policy_number" : "123456",
                                                 "coverage_details" : "detail coverage"
                                                 })
        
    def action_print_appointments(self): #accion para devolver un boton para hacer impresion de reports
        appointments = self.appointment_ids
        report = self.env.ref("veterinary_clinic_juan_carlos.action_report_veterinary_appointment").report_action(appointments.ids)
        if appointments:
            return report 
        else: raise ValidationError("No appointments in this pet")
    