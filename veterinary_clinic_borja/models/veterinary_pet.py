from odoo import fields, models

class VeterinaryPet(models.Model):
   _name = "veterinary.pet"
   _description = "Veterinary Pet"

   name = fields.Char(string="Name", required=True, help="Name of the pet")
   birthdate = fields.Date(string="Birthdate", help="Birthdate of the pet")
   weight = fields.Float(string="Weight", help="Weight of the pet")
   age = fields.Integer(string="Age")
   pet_number = fields.Char(string="Pet Number", help="Chip number of the pet")
   species = fields.Selection([
    ("cat", "Cat"),
    ("dog", "Dog"),
    ("bird", "Bird"),
    ("other", "Other")
   ])