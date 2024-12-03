from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    appointment_id = fields.Many2one('veterinary.appointment')
