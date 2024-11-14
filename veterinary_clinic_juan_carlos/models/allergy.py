from odoo import fields, models

class Allergy(models.Model):
    _name = "veterinary.allergy"
    _description = "Veterinary allergy"

    name = fields.Char(string="Name", required=True, help="Name of the allergy")
    severity_level = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ], string="Severity Level", help="Indicates the severity level of the allergy")
    allergy_description = fields.Text(string="Allergy description")
