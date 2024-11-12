from odoo import models, fields


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary appointment'

    name = fields.Char(string='Name', required=True)
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    reason = fields.Text(string='Reason')
    solution = fields.Html(string='Solution')
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='draft'
    )
    duration = fields.Float(string='Duration (minutes)', help='Duration in minutes')
    user_id = fields.Many2one('res.users', string='Responsible')
    sequence = fields.Integer(string='Sequence')
    urgency = fields.Boolean(string='Urgency')