from odoo import fields, models

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