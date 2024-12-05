from odoo import models, fields, api

class VeterinaryAppointmentLine(models.Model):
    _name = 'veterinary.appointment.line'
    _description = 'Veterinary Appointment Line'

    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    appointment_id = fields.Many2one('veterinary.appointment', string='Appointment', required=True)
    qty = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Monetary(string='Unit Price', required=True)
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_price_subtotal', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    @api.depends('qty', 'price_unit')
    def _compute_price_subtotal(self):
        for line in self:
            line.price_subtotal = line.qty * line.price_unit