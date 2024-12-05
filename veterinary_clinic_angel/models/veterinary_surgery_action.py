from odoo import models, fields

class VeterinarySurgeryAction(models.Model):
    _name = 'veterinary.surgery.action'
    _description = 'Veterinary Surgery Action'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status',)
    surgery_id = fields.Many2one('veterinary.surgery', string='Surgery', required=True)