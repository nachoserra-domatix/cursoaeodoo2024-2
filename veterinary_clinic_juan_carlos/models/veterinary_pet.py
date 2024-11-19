from odoo import models, fields, api
import random
import string

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
    # species = fields.Selection([
    #     ("cat", "Cat"),
    #     ("dog", "Dog"),
    #     ("other", "Other"),
    #     ("bird", "Bird"),
    # ])
    vaccinated = fields.Boolean(string="Vaccinated", compute="_compute_vaccinated", inverse="_inverse_vaccinated", store=True)
    last_vaccination_date = fields.Date(string="Last Vaccination Date")
    
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