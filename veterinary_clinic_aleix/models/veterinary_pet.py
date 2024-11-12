from odoo import models, fields

class VeterinaryPet(models.Model):
   _name = 'veterinary.pet'
   _description = 'Veterinary Pet'

   name = fields.Char(string='Name', required=True, help='Name of the pet')
   birthday = fields.Date(string='Birthday', help='Birthday of the pet')
   weight = fields.Float(string='Weight', help='Weight of the pet')
   age = fields.Integer(string='Age', help='Age of the pet')
   pet_number = fields.Char(string='Pet Number', help='Number of the pet')

   species = fields.Selection(
      [('cat', 'Cat'), ('dog', 'Dog'), ('bird', 'Bird'), ('other', 'Other')],
      string='Species'
    )

