from odoo import fields, models


class VeterinaryInsurance(models.Model):
    _inherit = "veterinary.insurance"

    order_id = fields.Many2one("sale.order", string="Sale order")