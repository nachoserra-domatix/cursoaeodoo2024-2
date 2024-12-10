from odoo import models, fields,api
import random
from datetime import date

class VeterinaryPet(models.Model):
    _name= 'veterinary.pet'
    _description = 'Veterinary Pet'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the pet')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age', compute='_compute_age',search='_search_age')
    number_pet=fields.Char(string='Pet Number', help='Number of the pet', copy=False, tracking=True) #Permite que no se duplique el campo al copiar

    species_id = fields.Many2one('veterinary.species', string='Species', help='Species of the pet')
    description = fields.Text(string='Description', help='Description of the pet')

    vaccinated = fields.Boolean(string='Vaccinated', compute = '_is_vacinated', inverse='_inverse_vaccinated',store=True)
    last_vaccination_date = fields.Date(string='Last Vaccination Date', help='Last vaccination date of the pet')
    image = fields.Image()
    alergy_ids = fields.Many2many('veterinary.allergy', string='Allergies')
    is_adopted = fields.Boolean(string='Is Adopted', help='Is adopted pet')
    appointment_ids = fields.One2many('veterinary.appointment', 'pet_id', string='Appointments', help='Appointments of the pet')
    appointment_count = fields.Integer(string='Appointment Count', compute='compute_apointment_count')
    insurance_count = fields.Integer(string='Insurance Count', compute='_compute_insurance_count')
    surgery_count = fields.Integer(string='Insurance Count', compute='_compute_surgery_count')
    insurance_ids = fields.One2many('veterinary.insurance', 'pet_id', string='Insurances', help='Insurances of the pet')
    active = fields.Boolean(string='Active', default=True)


    _sql_constraints = [
        ('number_unique_specie', 'UNIQUE(number_pet,species_id)', 'The number must be unique for each specie') #Restringe que solo exista un numero por especie
    ]

    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = self.env['veterinary.insurance'].search_count([('pet_id', '=', self.id)])

    def _compute_surgery_count(self):
        for record in self:
            record.surgery_count = self.env['veterinary.surgery'].search_count([('pet_id', '=', self.id)])


    def action_print_appointments(self):
        appointments = self.appointment_ids

        return self.env.ref('veterinary_clinic_alex.action_report_veterinary_appointment').report_action(appointments.ids) #devuelve un registro a partir de un xml id, permite imprimir las ids que se le pasan
    
    def compute_apointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def action_view_surgery_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Surgery History',
            'res_model': 'veterinary.surgery',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }
    def action_view_insurance_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurance History',
            'res_model': 'veterinary.insurance',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }

    def action_view_medical_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical History',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'domain': [('pet_id', '=', self.id)],
        }

    def _inverse_vaccinated(self):
        for record in self:
            if not record.vaccinated:
                record.last_vaccination_date = fields.Date.today()

    @api.depends('last_vaccination_date')
    def _is_vacinated(self):
        for record in self:
            record.vaccinated = bool(record.last_vaccination_date)
    
  
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365

    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def action_number_pet(self):
        for record in self:
            record.number_pet ='ES' + str(random.randint(1,9999999999999))


    def create_insurance(self):
        self.env['veterinary.insurance'].create({'insurance_company': 'Asisa', 
                                                 'insurance_number': '1234',})
        
    def complete_surgery(self):       
       surgery_ids = self.env['veterinary.surgery'].search([('pet_id' , '=', self.id)])
       surgery_ids.action_done()


    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365
            else:
                record.age = 0

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
    