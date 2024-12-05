from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_insurance = fields.Boolean(string='Is Insurance')