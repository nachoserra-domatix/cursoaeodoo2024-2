from odoo import fields, models
import random
import string

class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age')
    pet_number = fields.Char(string='Pet Number', help='Number of the pet')
    species = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other')
    ], string='Species', default='dog')
    notes = fields.Text(string='Notes')
    vaccinated = fields.Boolean(string='Vaccinated', default=False)
    last_vaccination_date = fields.Date(string='Last Vaccination Date')

    def action_vaccinated(self):
        self.vaccinated = True
        self.last_vaccination_date = fields.Date.today()

    def action_get_pet_number(self):
        while True:
            pet_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=6))
            if not self.env['veterinary.pet'].search([('pet_number', '=', pet_number)]):
                self.pet_number = pet_number
                break