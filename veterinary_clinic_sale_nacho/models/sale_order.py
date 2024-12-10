from odoo import fields,models,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    appointment_id = fields.Many2one('veterinary.appointment', string='Appointment')
    insurance_count = fields.Integer(string='Insurance Count', compute='_compute_insurance_count')
    
    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = self.env['veterinary.insurance'].search_count([('order_id', '=', self.id)])
    
    def action_view_insurances(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurances',
            'res_model': 'veterinary.insurance',
            'view_mode': 'tree,form',
            'domain': [('order_id', '=', self.id)],
        }

    def action_confirm(self):
        res = super().action_confirm()
        insurance_line = self.order_line.filtered(lambda self: self.product_id.is_insurance)
        if insurance_line:
            for pet in self.partner_id.pet_ids:
                self.create_insurance(pet)
        return res
    
    def create_insurance(self, pet):
        insurance = self.env['veterinary.insurance'].create({
           'pet_id': pet.id,
           'policy_number': self.name + '-' + pet.name,
           'insurance_company': self.company_id.name,
           'coverage': 'Complete coverage',
           'order_id': self.id,
        })
        insurance.message_post_with_source(
            'mail.message_origin_link',
            render_values={'self': insurance, 'origin': self},
            subtype_xmlid='mail.mt_note'
        )