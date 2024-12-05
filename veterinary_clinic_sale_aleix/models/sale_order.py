from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Many2one
    appointment_id = fields.Many2one('veterinary.appointment')
    # One2many
    insurance_ids = fields.One2many(
        comodel_name='veterinary.insurance', inverse_name='order_id')
    insurance_count = fields.Integer(
        string='Insurance Count', compute='_compute_insurance_count')

    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = len(record.insurance_ids)

    def action_view_insurances(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurances',
            'res_model': 'veterinary.insurance',
            'view_mode': 'tree,form,kanban',
            'domain': [('order_id', '=', self.id)],
        }

    # overwrite
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id and line.product_id.insurance:
                    # create insurance
                    insurance = self.env['veterinary.insurance'].create(
                        {'order_id': order.id,
                            'insurance_company': line.product_id.name,
                         })
                    # insurance.message_post(
                    #     body=f"Insurance created from {order.name} order",
                    #     message_type="notification")
                    insurance.message_post_with_source(
                        'mail.message_origin_link',
                        render_values={
                            'self': insurance,
                            'origin': self},
                        subtype_xmlid='mail.mt_note',
                    )
        return res
