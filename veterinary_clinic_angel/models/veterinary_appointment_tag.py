from odoo import models, fields

class VeterinaryAppointmentTag(models.Model):
    _name = 'veterinary.appointment.tag'
    _description = 'Veterinary Appointment Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color Index', default=0)