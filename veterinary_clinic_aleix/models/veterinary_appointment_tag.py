from odoo import models, fields, api


class VeterinaryAppointmentTag(models.Model):
    _name = 'veterinary.appointment.tag'
    _description = 'Veterinary Appointment Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')



