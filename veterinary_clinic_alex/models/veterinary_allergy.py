from odoo import models, fields, api

class VeterinaryAllergy(models.Model):
    _name= 'veterinary.allergy'
    _description = 'Veterinary Allergy'

    name = fields.Char(string='Name', required=True)
    severity_grade = fields.Selection([('low','Low'),('medium','Medium'),('high','High')], string='Severity Grade', required=True)
    description = fields.Text(string='Description', help='Description of the allergy')
    is_severity = fields.Boolean(string='Is Severity', help='Severity of the allergy', compute='_compute_is_severity', store=True)

    @api.depends('severity_grade')
    def _compute_is_severity(self):
        for record in self:
            if record.severity_grade == 'high':
                record.is_severity = True
            else:
                record.is_severity = False