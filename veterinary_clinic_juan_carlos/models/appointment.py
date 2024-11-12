from odoo import models, fields

class Appointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    _rec_name = "reason" #actua como nombre

    appointment_date = fields.Datetime(string="Appointment Date", help="Date and time", default=fields.Datetime.now)
    reason = fields.Text(string="Reason for Appointment", help="reason")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default="draft", help="current status of the appointment")
    duration = fields.Float(string="Duration (minutes)", help="Duration minutes")
    