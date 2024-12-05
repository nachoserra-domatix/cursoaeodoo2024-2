from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # One2many
    pet_ids = fields.One2many(
        comodel_name='veterinary.pet', inverse_name='partner_id')
    pet_count = fields.Integer(
        string='Pet Count', compute='_compute_pet_count')

    def _compute_pet_count(self):
        for record in self:
            record.pet_count = len(record.pet_ids)

    def action_view_pets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pets',
            'res_model': 'veterinary.pet',
            'view_mode': 'tree,form,kanban',
            'domain': [('partner_id', '=', self.id)],
        }
