from odoo import models, fields, api


class VeterinaryAllergy(models.Model):
    _name = 'veterinary.allergy'
    _description = 'Veterinary Allergy'

    name = fields.Char(string='Name', required=True)
    severity_degree = fields.Selection(
        selection=[('low', 'Low'), ('medium', 'Medium'),
                   ('high', 'High'), ('severe', 'Severe')],
        string='State',
        required=True
    )
    description = fields.Text(string='Description')

    # computed fields
    is_severe = fields.Boolean(
        string='Is Severe', compute='_compute_is_severe', store=True)

    # computed methods
    @api.depends('severity_degree')
    def _compute_is_severe(self):
        for record in self:
            if record.severity_degree == 'severe':
                record.is_severe = True
            else:
                record.is_severe = False
