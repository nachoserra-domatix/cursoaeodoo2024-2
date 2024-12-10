from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    pet_ids = fields.Many2many('veterinary.pet', 'partner_pet_rel', 'partner_id', 'pet_id', string='Pets')
    pet_count = fields.Integer(string='Pet Count', compute='_compute_pet_count')


    def _compute_pet_count(self):
        for record in self:
            record.pet_count = len(record.pet_ids)

    def action_view_pets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Pets',
            'res_model': 'veterinary.pet',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.pet_ids.ids)],
            'context': {'default_partner_ids': [(4, self.id)]}
        }