from odoo import fields, models, api


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
    is_severe = fields.Boolean(string='Is Severe', compute='_compute_is_severe', store=True)


    @api.depends('severity')
    def _compute_is_severe(self):
        for record in self:
            if record.severity == 'severe':
                record.is_severe = True
            else:
                record.is_severe = False
