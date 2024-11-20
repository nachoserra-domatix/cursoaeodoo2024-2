from odoo import fields, models


class VeterinarySurgeryLine(models.Model):
    _name = 'veterinary.surgery.line'
    _description = 'Veterinary Surgery'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done')
        ], default='draft', string='State')
    # Many2one
    surgery_id = fields.Many2one('veterinary.surgery', string='Surgery')
