from odoo import models, fields

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
    ], string='Status', default='scheduled')

    def action_start_surgery(self):
        self.state = 'in_progress'
    
    def action_finish_surgery(self):
        self.state = 'done'

    def action_cancel_surgery(self):
        self.state = 'cancelled'