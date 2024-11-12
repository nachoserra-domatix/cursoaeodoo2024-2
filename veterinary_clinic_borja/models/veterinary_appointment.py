from odoo import fields, models

class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # Name by defect is reason
    # _rec_name = "reason"

    name = fields.Char(string="Name", required=True)
    date = fields.Datetime(string="Date", required=True)
    reason = fields.Text(string="Reason", required=True)
    solution = fields.Html(string="Solution")
    status = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status")
    duration_minutes = fields.Integer(string="Duration", required=True, help="Duration in minutes")
    user_id = fields.Many2one("res.users", string="Responsible")
    sequence = fields.Integer(string="Sequence", default=10)
    urgency = fields.Boolean(string="Urgency")