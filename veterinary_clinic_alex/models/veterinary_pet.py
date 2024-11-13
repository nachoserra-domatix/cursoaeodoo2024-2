from odoo import models, fields
import random

class VeterinaryPet(models.Model):
    _name= 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthdate = fields.Date(string='Birthdate', help='Birthdate of the pet')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age')
    number_pet=fields.Char(string='Pet Number', help='Number of the pet')
    species = fields.Selection([
        ('cat', 'Cat'),
        ('dog', 'Dog'),
        ('bird', 'Bird'),
        ('other', 'Other')
    ])
    description = fields.Text(string='Description', help='Description of the pet')

    vaccinated = fields.Boolean(string='Vaccinated', help='Vaccinated pet')
    last_vaccination_date = fields.Date(string='Last Vaccination Date', help='Last vaccination date of the pet')


    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def action_number_pet(self):
        for record in self:
            record.number_pet ='ES' + str(random.randint(1,9999999999999))