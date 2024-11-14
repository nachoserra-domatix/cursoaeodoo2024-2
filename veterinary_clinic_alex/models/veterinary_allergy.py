from odoo import models, fields

class VeterinaryAllergy(models.Model):
    _name= 'veterinary.allergy'
    _description = 'Veterinary Allergy'

    name = fields.Char(string='Name', required=True)
    severity_grade = fields.Selection([('low','Low'),('medium','Medium'),('high','High')], string='Severity Grade', required=True)
    description = fields.Text(string='Description', help='Description of the allergy')