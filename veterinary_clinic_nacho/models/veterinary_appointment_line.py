from odoo import models, fields, api, Command


class VeterinaryAppointmentLine(models.Model):
    _name = 'veterinary.appointment.line'
    _description = 'Veterinary Appointment Lines'

    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Unit Price')
    appointment_id = fields.Many2one('veterinary.appointment', string='Appointment')
    subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related="appointment_id.currency_id")

    @api.depends('qty', 'price_unit')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.price_unit