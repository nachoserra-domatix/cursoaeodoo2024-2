from odoo import models, fields, api

class AppointmentLine(models.Model):
    _name = "veterinary.appointment.line"
    _description = "Veterinary Appointment Line"

    name = fields.Char(string="Name", required=True)
    product_id = fields.Many2one("product.product", string="Product")
    qty = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Price Unit", default=1.0)
    appointment_id = fields.Many2one("veterinary.appointment", string="Appointment")
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('qty', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.price_unit
