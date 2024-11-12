from odoo import models, fields


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary appointment'

    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    reason = fields.Text(string='Reason')

    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='draft'
    )

    duration = fields.Float(string='Duration (minutes)', help='Duration in minutes')
