from odoo import models, fields, api

class AppointmentLine(models.Model):
    _name = "veterinary.appointment.line"
    _description = "Veterinary Appointment Line"

    name = fields.Char(string="Name", required=True)
    product_id = fields.Many2one("product.product", string="product")
    qty = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Price Unit")
    appointment_id = fields.Many2one("veterinary.appointment", string="appointment")
    