from odoo import fields, models

class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"

    date = fields.Datetime(string="Date", required=True)
    reason = fields.Char(string="Reason", required=True)
    status = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ])
    duration_minutes = fields.Integer(string="Duration", required=True, help="Duration in minutes")