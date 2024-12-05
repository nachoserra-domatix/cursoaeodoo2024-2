from odoo import models, fields, api


class VeterinaryInsurance(models.Model):
    _inherit = 'veterinary.insurance'

    order_id = fields.Many2one('sale.order', string='Sale Order')