from odoo import models, fields, api

class VeterinarySurgery(models.Model):
    _name = 'veterinary.surgery'
    _description = 'Veterinary Surgery'

    name = fields.Char(string='Surgery Name', required=True)
    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    employee_id = fields.Many2one('hr.employee', string='Veterinarian', required=True)
    date = fields.Date(string='Surgery Date', required=True)
    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled',group_expand='_group_expand_states')
    color = fields.Integer(string='Color')
    action_ids = fields.One2many('veterinary.surgery.action', 'surgery_id',string='Actions')

    @api.model
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    
    def action_start_surgery(self):
        self.state = 'in_progress'
    
    def action_finish_surgery(self):
        self.state = 'done'

    def action_cancel_surgery(self):
        self.state = 'cancelled'