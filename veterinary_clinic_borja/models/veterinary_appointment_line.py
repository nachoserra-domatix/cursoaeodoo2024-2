from odoo import fields, models, api, Command


class VeterinaryAppointmentLine(models.Model):
    _name = "veterinary.appointment.line"
    _description = "Veterinary Appointment Lines"

    name = fields.Char(string="Name", required=True)
    product_id = fields.Many2one("product.product", string="Product")
    qty = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Unit Price")
    appointment_id = fields.Many2one("veterinary.appointment", string="Appointment")
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        related="appointment_id.currency_id",
        store=True,
    )
    subtotal = fields.Monetary(string="Subtotal", currency_field="currency_id")
