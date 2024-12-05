from odoo import fields, models, api

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
    is_severe = fields.Boolean(string="Is it severe?", store=True, compute= "_compute_is_severe")

    @api.depends("severity_level")
    def _compute_is_severe(self):
        for record in self:
            if record.severity_level == "severe":
                record.is_severe = True
            else:
                record.is_severe = False
