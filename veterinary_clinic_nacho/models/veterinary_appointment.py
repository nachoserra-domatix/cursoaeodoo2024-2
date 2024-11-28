from odoo import models, fields


class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    _rec_name = "reason"

    date = fields.Datetime(
        string="Date",
        required=True,
        help="Date of the appointment",
        default=fields.Datetime.now,
    )
    reason = fields.Text(string="Reason", help="Reason for the appointment")
    state = fields.Selection(
        [("draft", "Draft"), ("done", "Done"), ("cancel", "Cancel")],
        default="draft",
        string="State",
    )
    duration = fields.Float(string="Duration")
