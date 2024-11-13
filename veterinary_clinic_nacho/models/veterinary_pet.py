from odoo import models, fields
import random

class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the pet')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age')
    pet_number = fields.Char(string='Pet Number', help='Number of the pet')
    species = fields.Selection([
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('other', 'Other')
    ])
    vaccinated = fields.Boolean(string='Vaccinated')
    last_vaccination_date = fields.Date(string='Last Vaccination Date')

    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def generate_pet_number(self):
        for record in self:
            record.pet_number = ''.join(random.choices('ABCDFG1234',k=8))
