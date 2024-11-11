from odoo import models, fields, api

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'
    _rec_name = 'reason'

    reason = fields.Char(string='Reason', required=True)
    date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')
    duration = fields.Float(string='Duration')