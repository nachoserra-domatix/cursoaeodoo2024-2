from odoo import models, fields

class VeterinaryAllergy(models.Model):
    _name = 'veterinary.allergy'
    _description = 'Veterinary Allergy'

    name = fields.Char(string='Allergy Name', required=True)
    description = fields.Text(string='Description')
    severity = fields.Selection([
        ("0", 'Very low'),
        ("1", 'Low'),
        ("2", 'Moderate'),
        ("3", 'Severe')
    ], string='Severity', default='0')