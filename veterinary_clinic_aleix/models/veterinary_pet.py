from odoo import models, fields
import random

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
   vaccinated = fields.Boolean(string="Vaccinated", default=False)
   last_vaccination_date = fields.Date(string="Last Vaccination Date")

   # methods
   def action_vaccinated(self):
      for record in self:
         record.vaccinated = True
         record.last_vaccination_date = fields.Date.today()

   def action_random_pet_number(self):
         for record in self:
            record.pet_number = 'PET-' + str(random.randint(1,999999))
