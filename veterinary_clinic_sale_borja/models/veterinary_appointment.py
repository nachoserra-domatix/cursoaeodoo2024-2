from odoo import fields, models


class VeterinaryAppointment(models.Model):
    _inherit = "veterinary.appointment"

    order_id = fields.Many2one("sale.order", string="Order")
    order_count = fields.Integer(string="Order Count", compute="_compute_order_count")

    def _compute_order_count(self):
        for rec in self:
            rec.order_count = self.env["sale.order"].search_count(
                [("appointment_id", "=", rec.id)]
            )

    # def action_done(self):
    #     res = super().action_done()

    def action_confirm_sale(self):
        for rec in self:
            if rec.order_id:
                rec.order_id.action_confirm()
                rec.order_id._create_invoices()

    def action_cancelled(self):
        res = super().action_cancelled()
        orders = self.env["sale.order"].search([("appointment_id", "=", self.id)])
        for order in orders:
            order.action_cancel()
            order.unlink()
        return res

    def create_order(self):
        for rec in self:
            vals = {
                "partner_id": rec.partner_id.id,
                "appointment_id": rec.id,
                "date_order": rec.date,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": line.product_id.id,
                            "product_uom_qty": line.qty,
                            "price_unit": line.price_unit,
                            "name": line.name or line.product_id.name,
                        },
                    )
                    for line in rec.line_ids
                ],
            }
            order = self.env["sale.order"].create(vals)
            rec.order_id = order.id
            return {
                "name": "Sale Order",
                "type": "ir.actions.act_window",
                "res_model": "sale.order",
                "view_mode": "form",
                "res_id": order.id,
            }

    def action_view_order(self):
        return {
            "name": "Sale Order",
            "type": "ir.actions.act_window",
            "res_model": "sale.order",
            "view_mode": "tree,form",
            "domain": [("appointment_id", "=", self.id)],
        }
