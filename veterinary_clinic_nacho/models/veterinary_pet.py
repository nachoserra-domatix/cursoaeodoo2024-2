from odoo import models, fields, api
import random
from datetime import date

class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the pet')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age', compute='_compute_age', search='_search_age')
    pet_number = fields.Char(string='Pet Number', help='Number of the pet', copy=False)
    species_id = fields.Many2one('veterinary.species', string='Species', help='Species of the pet')
    vaccinated = fields.Boolean(string='Vaccinated', compute="_compute_vaccinated", inverse="_inverse_vaccinated")
    last_vaccination_date = fields.Date(string='Last Vaccination Date')
    photo = fields.Image(string='Photo')
    allergy_ids = fields.Many2many('veterinary.allergy', string='Allergies')
    adopted = fields.Boolean(string='Adopted', help='Adopted pet')
    appointment_ids = fields.One2many('veterinary.appointment', 'pet_id', string='Appointments')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def action_view_medical_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical History',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form,kanban',
            'domain': [('pet_id', '=', self.id)],
        }


    def _compute_vaccinated(self):
        for record in self:
            record.vaccinated = bool(record.last_vaccination_date)
    
    def _inverse_vaccinated(self):
        for record in self:
            if record.vaccinated:
                record.last_vaccination_date = fields.Date.today()
            else:
                record.last_vaccination_date = False

    def _search_age(self, operator, value):
        today = date.today()
        if operator in ('=', '!='):
            birth_year = today.year - value
            start_date = date(birth_year, today.month, today.day)
            end_date = date(birth_year - 1, today.month, today.day)
            return [('birthdate', '>=', end_date), ('birthdate', '<=', start_date)]
        elif operator in ('>', '>='):
            birth_year = today.year - value
            return [('birthdate', '<=', date(birth_year, today.month, today.day))]
        elif operator in ('<', '<='):
            birth_year = today.year - value
            return [('birthdate', '>=', date(birth_year + 1, today.month, today.day))]
        else:
            return []

    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365
            else:
                record.age = 0

    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def generate_pet_number(self):
        for record in self:
            record.pet_number = ''.join(random.choices('ABCDFG1234',k=8))
    
    def create_insurance(self):
        self.env['veterinary.insurance'].create({'policy_number': '1234',
                                                  'insurance_company': 'AXA',})
    
    def check_all_surgery_as_done(self):
        surgeries = self.env['veterinary.surgery'].search([('pet_id', '=', self.id)])
        surgeries.action_done()
        
