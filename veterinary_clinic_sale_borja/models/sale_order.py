import random
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    appointment_id = fields.Many2one("veterinary.appointment", string="Appointment")

    def action_confirm(self):
        self.ensure_one()
        res = super().action_confirm()
        for line in self.appointment_id.line_ids:
            if line.product_id.insurance:
                insurance = {
                    "pet_id": self.appointment_id.pet_id.id,
                    "sale_id": self.id,
                    "insurance_company": "Allianz",
                    "policy_number": random.randint(1, 10000),
                    "coverage_details": "Insurance from sale order",
                }
                self.env["veterinary.insurance"].create(insurance)
        return res
