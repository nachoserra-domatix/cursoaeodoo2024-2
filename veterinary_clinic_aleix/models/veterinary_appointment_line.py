from odoo import models, fields, api


class VeterinaryAppointmentLine(models.Model):
    _name = 'veterinary.appointment.line'
    _description = 'Veterinary Appointment Line'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    # Many2one
    appointment_id = fields.Many2one('veterinary.appointment', string='Appointment')


