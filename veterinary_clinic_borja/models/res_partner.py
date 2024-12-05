from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    pet_ids = fields.One2many("veterinary.pet", "partner_id", string="Pets")
    pets_count = fields.Integer(string="Pets Count", compute="_compute_pets_count")

    def _compute_pets_count(self):
        for rec in self:
            rec.pets_count = len(self.pet_ids)

    def partner_pets(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Pets",
            "res_model": "veterinary.pet",
            "view_mode": "tree,form",
            "domain": [("id", "in", self.pet_ids.mapped("id"))],
        }
