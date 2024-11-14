from odoo import fields, models


class VeterinaryAllergy(models.Model):
    _name = 'veterinary.allergy'
    _description = 'Veterinary Allergy'

    name = fields.Char(string='Name', required=True, help='Name of the allergy')
    description = fields.Text(string='Description', help='Description of the allergy')
    severity = fields.Selection([
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe')
    ], string='Severity', help='Severity of the allergy')