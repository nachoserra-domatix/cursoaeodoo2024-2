from odoo import models, fields

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'
    _rec_name = 'reason' # Permite establecer el campo que va actuar como name cuando el campo name no exista 


    date = fields.Datetime(string='Date', required=True, default =fields.Datetime.now, help='Date of the appointment')
    reason = fields.Text(string='Reason', help='Description of the appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft', string='State', help='State of the appointment')

    duration = fields.Float(string='Duration', help='Duration of the appointment')