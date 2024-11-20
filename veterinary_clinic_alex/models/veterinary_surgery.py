from odoo import models, fields

class VeterinarySurgery(models.Model):

    _name = 'veterinary.surgery'
    _description = 'Veterinary Surgery'

    name = fields.Char(string='Name', required=True)
    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    surgery_date = fields.Datetime(string='Surgery Date', required=True)
    surgery_state = fields.Selection([
        ('pending', 'Pending'),
        ('procces', 'In Procces'),
        ('done', 'Done')
    ], default='pending', string='State', help='State of the appointment', group_expand = '_group_expand_states')
    color = fields.Integer(string="Color")
    line_ids = fields.One2many('veterinary.surgery.line', 'surgery_id', string='Steps')
    
    
    def action_procces(self):
        for record in self:
            record.surgery_state = 'procces'

    def action_done(self):
        for record in self:
            record.surgery_state = 'done'

    def action_pending(self):
        for record in self:
            record.surgery_state = 'pending'

    def _group_expand_states(self,states,domian,order):
        return [key for key, val in type(self).surgery_state.selection]
    