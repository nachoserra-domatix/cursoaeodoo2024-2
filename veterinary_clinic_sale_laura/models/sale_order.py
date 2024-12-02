from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit='sale.order'

    appointment_id=fields.Many2one('veterinary.appointment',string="Appointment")