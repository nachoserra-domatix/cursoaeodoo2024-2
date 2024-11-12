from odoo import fields, models

class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # Name by defect is reason
    _rec_name = "reason"

    date = fields.Datetime(string="Date", required=True)
    reason = fields.Char(string="Reason", required=True)
    status = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status")
    duration_minutes = fields.Integer(string="Duration", required=True, help="Duration in minutes")
    user_id = fields.Many2one("res.users", string="Responsible")