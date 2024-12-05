import random
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    appointment_id = fields.Many2one("veterinary.appointment", string="Appointment")
    insurance_count = fields.Integer(
        string="Insurance Count", compute="_compute_insurance_count"
    )

    def _compute_insurance_count(self):
        self.ensure_one()
        self.insurance_count = len(
            self.env["veterinary.insurance"].search([("order_id", "=", self.id)])
        )

    def action_insurance(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Insurances",
            "res_model": "veterinary.insurance",
            "view_mode": "tree,form",
            "domain": [("order_id", "=", self.id)],
        }

    def action_confirm(self):
        self.ensure_one()
        res = super().action_confirm()
        # insurance_line = self.order_line.filtered(lambda self: self.product_id.insurance)
        # if insurance_line:
        #    self._create_insurance()
        for line in self.appointment_id.line_ids:
            if line.product_id.insurance:
                self._create_insurance()
        return res

    def _create_insurance(self):
        insurance = {
            "pet_id": self.appointment_id.pet_id.id,
            "order_id": self.id,
            "insurance_company": "Allianz",
            "policy_number": random.randint(1, 10000),
            "coverage_details": "Insurance from sale order",
        }
        self.env["veterinary.insurance"].create(insurance)
