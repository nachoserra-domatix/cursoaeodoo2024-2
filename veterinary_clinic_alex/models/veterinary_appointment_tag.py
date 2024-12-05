from odoo import models, fields, api

class VeterinaryAppointmentTag(models.Model):
    _name = 'veterinary.appointment.tag'
    _description = 'Veterinary Appointment Tags'
    
    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color', default=0)