from odoo import models, fields, api

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    reason = fields.Char(string='Reason', required=True)
    solution = fields.Html(string='Solution', help='Solution of the appointment')
    date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')
    duration = fields.Float(string='Duration')
    user_id = fields.Many2one('res.users', string='Responsible')
    sequence = fields.Integer(string='Sequence', default=10)
    urgency = fields.Boolean(string='Urgent')