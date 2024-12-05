from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    insurance = fields.Boolean(string='Is Insurance', default=False)
