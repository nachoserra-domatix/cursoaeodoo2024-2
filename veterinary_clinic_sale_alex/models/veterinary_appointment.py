from odoo import models, fields, api

class VeterinaryAppointment(models.Model):
    _inherit = 'veterinary.appointment'

    order_id = fields.Many2one('sale.order', string='Order')
    order_count = fields.Integer(compute='_compute_order_count', string='Order Count')

    def _compute_order_count(self):
        for record in self:
            record.order_count = self.env['sale.order'].search_count([('appointment_id', '=', record.id)])

    def create_order(self):
        for record in self:
            vals ={'partner_id': record.partner_id.id,
                   'appointment_id': record.id,
                   'date_order': record.date,
                   'order_line': [(0, 0, {'product_id': line.product_id.id,
                                          'product_uom_qty': line.qty,
                                          'price_unit': line.price_unit,
                                          'name':line.name or line.product_id.name}) for line in record.line_ids]
                   }
            order = self.env['sale.order'].create(vals)
            record.order_id = order.id
            return {
                'name': 'Sale Order',
                'view_mode': 'form',
                'res_model': 'sale.order',
                'res_id': order.id,
                'type': 'ir.actions.act_window',
            }
        
    def action_view_order(self):
        return {
                'name': 'Sale Order',
                'view_mode': 'tree,form',
                'res_model': 'sale.order',
                'type': 'ir.actions.act_window',
                'domain': [('appointment_id', '=', self.id)],
            }

       
