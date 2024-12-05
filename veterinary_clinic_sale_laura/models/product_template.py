from odoo import models, fields, api
import random
import string
from datetime import date
from odoo.exceptions import UserError, ValidationError, AccessDenied

class ProductTemplate(models.Model):
    _inherit="product.template"

    is_insurance=fields.Boolean(string="Insurance",default=False)