from odoo import models, fields,api
import random

class VeterinaryPet(models.Model):
    _name= 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the pet',required=True)
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age', compute='_compute_age',search='_search_age')
    number_pet=fields.Char(string='Pet Number', help='Number of the pet', copy=False) #Permite que no se duplique el campo al copiar

    species_id = fields.Many2one('veterinary.species', string='Species', help='Species of the pet')
    description = fields.Text(string='Description', help='Description of the pet')

    vaccinated = fields.Boolean(string='Vaccinated', compute = '_is_vacinated', inverse='_inverse_vaccinated',store=True)
    last_vaccination_date = fields.Date(string='Last Vaccination Date', help='Last vaccination date of the pet')
    image = fields.Image()
    alergy_ids = fields.Many2many('veterinary.allergy', string='Allergies')
    is_adopted = fields.Boolean(string='Is Adopted', help='Is adopted pet')


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