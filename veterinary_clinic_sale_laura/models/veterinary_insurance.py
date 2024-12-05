from odoo import models, fields

class VeterinaryInsurance(models.Model):
   _inherit = "veterinary.insurance"
   
   order_id=fields.Many2one('sale.order',string="Order")