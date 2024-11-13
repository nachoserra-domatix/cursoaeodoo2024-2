from odoo import models, fields
import random
import string

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
   sequence = fields.Integer(string="Sequence",default=10)
   user_id = fields.Many2one('res.users',string="Responsible")
   vaccinated = fields.Boolean(string="Vaccinated")
   last_vaccination_date=fields.Date(string="Last vaccination date")

   def action_vaccinated(self):
      for record in self:
         record.vaccinated=True
         record.last_vaccination_date=fields.Datetime.now()

   def action_set_pet_number(self):
      def generate_string():
         numeros = ''.join(random.choices(string.digits, k=8))  # 8 dígitos aleatorios
         letra = random.choice(string.ascii_uppercase)          # 1 letra aleatoria en mayúscula
         resultado = numeros + letra                            # Concatenamos números y letra
         return resultado
      
      for record in self:
         record.pet_number=generate_string()
