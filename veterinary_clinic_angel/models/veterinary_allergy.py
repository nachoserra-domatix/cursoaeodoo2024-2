from odoo import models, fields, api 

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
    is_severe = fields.Boolean(string='Is Severe', compute='_compute_is_severe', store=True)

    @api.depends('severity')
    def _compute_is_severe(self):
        for record in self:
            record.is_severe = record.severity == '3'