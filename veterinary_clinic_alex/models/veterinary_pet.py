from odoo import models, fields

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