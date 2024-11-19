from odoo import models, fields, api
import random
import string

class VeterinaryPet(models.Model):
   _name = "veterinary.pet"
   _description = "Veterinary Pet"

   name = fields.Char(string='Name',required=True,help='Name of the pet')
   birthdate = fields.Date(string='Birth Date')
   weight=fields.Float(string='Weight',help='Birth of the pet')
   age = fields.Integer(string="Age",compute="_compute_age",store=True)
   pet_number= fields.Char(string='Pet Number', help='Number of the pet')
   species_id= fields.Many2one('veterinary.species',string="Species")
   sequence = fields.Integer(string="Sequence",default=10)
   user_id = fields.Many2one('res.users',string="Responsible")
   vaccinated = fields.Boolean(string="Vaccinated",compute="_compute_vaccinated",inverse="_inverse_vaccinated")
   last_vaccination_date=fields.Date(string="Last vaccination date")

   
   def _compute_vaccinated(self):
      for record in self:
         if record.last_vaccination_date:
            record.vaccinated=True
         else:
            record.vaccinated=False
   
   def _inverse_vaccinated(self):
      for record in self:
         if record.vaccinated:
            record.last_vaccination_date=fields.Datetime.now().date()
   
   @api.depends('birthdate')
   def _compute_age(self):
      for record in self:
         if record.birthdate:
            record.age=(fields.Date.today() - record.birthdate).days //365
         else:
            record.age = 0

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

   def create_insurance(self):
      self.copy({'name':'Copy of '+self.name})
      #self.env['veterinary.insurance'].create({'name':'name',
      #                                         'policy_number':'1234',
      #                                         'insurance_company':'AXA'})
   
   def surgery_complete_pet(self):
      surgery_ids= self.env['veterinary.surgery'].search([('pet_id','=',self.id)])
      surgery_ids.action_finish()