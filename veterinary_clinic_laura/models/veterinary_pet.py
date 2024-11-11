from odoo import models, fields

class VeterinaryPet(models.Model):
   _name = "veterinary.pet"
   _description = "Veterinary Pet"

   name = fields.Char(string='Name',required=True,help='Name of the pet')
   birthdate = fields.Date(string='Birth Date')
   weight=fields.Float(string='Weight',help='Birth of the pet')
   age = fields.Integer(string="Age")
   pet_number= fields.Char(string='Pet Number', help='Number of the pet')
   species= fields.Selection([
      ('cat','Cat'),
      ('dog','Dog'),
      ('bird','Bird'),
      ('other','Other'),
   ])