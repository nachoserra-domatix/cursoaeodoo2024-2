from odoo import models, fields, api, _
from odoo.tools import date_utils
from odoo.exceptions import UserError, ValidationError

import logging
logger = logging.getLogger(__name__)


class VeterinaryInsurance(models.Model):
    _inherit = 'veterinary.insurance'

    # Many2one
    order_id = fields.Many2one('sale.order', string='Order')