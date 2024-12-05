from odoo import models, fields

class VeterinarySurgeryLine(models.Model):

    _name = 'veterinary.surgery.line'
    _description = 'Veterinary Surgery Lin'

    name = fields.Char(string='Name')
    sequence = fields.Integer(string='Sequence')
    state = fields.Selection([
        ('pending', 'Pending'),
        ('procces', 'In Procces'),
        ('done', 'Done')
        
    ], string='State', help='State of Surgery')

    surgery_id = fields.Many2one('veterinary.surgery', string='Surgery')