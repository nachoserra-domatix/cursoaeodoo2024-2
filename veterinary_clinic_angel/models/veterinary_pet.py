from odoo import fields, models, api
import random
import string

class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age', compute="_compute_age", store=True)
    pet_number = fields.Char(string='Pet Number', help='Number of the pet')
    species_id = fields.Many2one('veterinary.species', string='Species', required=True)
    notes = fields.Text(string='Notes')
    vaccinated = fields.Boolean(string='Vaccinated', default=False, compute="_compute_vaccinated", store=True, inverse="_inverse_vaccinated")
    last_vaccination_date = fields.Date(string='Last Vaccination Date')
    surgery_ids = fields.One2many('veterinary.surgery', 'pet_id', string='Surgeries')
    surgery_count = fields.Integer(string='Surgery Count', compute='_compute_surgery_count')
    image = fields.Image(string='Pet Photo')
    allergy_ids = fields.Many2many('veterinary.allergy', string='Allergies')
    adopted = fields.Boolean(string='Adopted', default=False)
    appointment_ids = fields.One2many('veterinary.appointment', 'pet_id', string='Appointments')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    insurance_ids = fields.One2many('veterinary.insurance', 'pet_id', string='Insurances')
    insurance_count = fields.Integer(string='Insurance Count', compute='_compute_insurance_count')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_pet_number_species', 'unique(pet_number,species_id)', 'The pet number and species must be unique'),
    ]

    @api.depends('surgery_ids')
    def _compute_surgery_count(self):
        for record in self:
            record.surgery_count = len(record.surgery_ids)

    @api.depends('insurance_ids')
    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = len(record.insurance_ids)

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    @api.depends('last_vaccination_date')
    def _compute_vaccinated(self):
        for record in self:
            record.vaccinated = bool(record.last_vaccination_date)
    
    def _inverse_vaccinated(self):
        for record in self:
            if not record.vaccinated:
                record.last_vaccination_date = False
            elif record.vaccinated and record.last_vaccination_date is False:
                record.last_vaccination_date = fields.Date.today()

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365

    def action_vaccinated(self):
        self.vaccinated = True
        self.last_vaccination_date = fields.Date.today()

    def action_get_pet_number(self):
        while True:
            pet_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=6))
            if not self.env['veterinary.pet'].search([('pet_number', '=', pet_number)]):
                self.pet_number = pet_number
                break

    def action_create_insurance(self):
        self.env['veterinary.insurance'].create({
            'pet_id': self.id,
            'policy_number': '1234',
        })

    def action_finish_surgeries(self):
        for surgery in self.surgery_ids:
            surgery.write({'state': 'done'})
            
    def action_view_medical_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical History',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }

    def action_view_insurances(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurances',
            'res_model': 'veterinary.insurance',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }

    def action_view_surgeries(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Surgeries',
            'res_model': 'veterinary.surgery',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }
    
    def action_print_appointments(self):
        appointments = self.appointment_ids
        return self.env.ref('veterinary_clinic_angel.action_report_appointments').report_action(appointments.ids)