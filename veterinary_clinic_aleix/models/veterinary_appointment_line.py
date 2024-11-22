from odoo import models, fields, api


class VeterinaryAppointmentLine(models.Model):
    _name = 'veterinary.appointment.line'
    _description = 'Veterinary Appointment Line'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity')
    price_unit = fields.Float(string='Price Unit')
    subtotal = fields.Float(string='Subtotal')
    # Many2one
    appointment_id = fields.Many2one('veterinary.appointment', string='Appointment')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    # computed
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    # computed methods
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
       for record in self:
            record.subtotal = record.quantity * record.price_unit


    

