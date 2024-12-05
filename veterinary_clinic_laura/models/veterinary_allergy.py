from odoo import models, fields, api

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
   is_severe=fields.Boolean(string="Is severe",compute="_compute_severe",store=True)
   
   @api.depends('severity_grade')
   def _compute_severe(self):
        for record in self:
            if record.severity_grade=='high':
                record.is_severe=True
            else:
                record.is_severe=False