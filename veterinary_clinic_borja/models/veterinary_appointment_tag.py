from odoo import fields, models, api

class veterinary_appointment_tag(models.Model):
    _name = "veterinary.appointment.tag"
    _description = "Veterinary Appointments Tags"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    color = fields.Integer(string="Color", default=0)