from odoo import fields, models

class VeterinarySurgeryActions(models.Model):
    _name = "veterinary.surgery.action"
    _description = "Veterinary Surgery Action"

    name = fields.Char(string="Name", required=True, help="Name of the action")
    sequence = fields.Integer(string="Sequence", default=10)
    status = fields.Selection([
        ("draft", "Draft"),
        ("in_progress", "In progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status")
    surgery_id = fields.Many2one("veterinary.surgery", string="Surgery")