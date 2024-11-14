from odoo import models, fields

class VeterinaryAllergy(models.Model):
   _name = "veterinary.allergy"
   _description = "Veterinary Allergy"

   name = fields.Char(string='Name',required=True,help='Name of the allergy')
   severity_grade= fields.Selection([
     ('low','Low'),
     ('medium','Medium'),
     ('high','High'),
   ],default='low', string='State')
   description=fields.Char(string="Description")