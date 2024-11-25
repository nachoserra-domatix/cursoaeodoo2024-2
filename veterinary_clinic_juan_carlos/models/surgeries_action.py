from odoo import models, fields

class SurgeriesAction(models.Model):
    _name = "veterinary.surgeries.action"
    _description = "Veterinary surgeries action"

    name = fields.Char(string="Action Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string="Status", help="Current status of the surgery")
    surgery_id = fields.Many2one("veterinary.surgeries", string="Surgery")