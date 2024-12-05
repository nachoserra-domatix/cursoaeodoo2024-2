from odoo import models, fields


class VeterinarySurgery(models.Model):
    _name = 'veterinary.surgery'
    _description = 'Veterinary Surgery'
    _order = 'surgery_date desc'

    name = fields.Char(string='Name', required=True)
    surgery_date = fields.Datetime(
        string='Surgery date', required=True, default=fields.Datetime.now)
    state = fields.Selection(
        selection=[('pending', 'Pending'), ('in_progress', 'In progress'), (
            'done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='pending',
        group_expand='_group_expand_states'
    )
    duration = fields.Float(string='Duration (minutes)', help='Duration in minutes')
    color = fields.Integer(string='Color')
    # Many2one
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    # One2many
    line_ids = fields.One2many('veterinary.surgery.line', 'surgery_id', string='Lines')

    # methods
    def action_pending(self):
        for record in self:
            record.state = 'pending'

    def action_in_progress(self):
        for record in self:
            record.state = 'in_progress'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancelled(self):
        for record in self:
            record.state = 'cancelled'

    # método odoo para forzar que salgan todos los estados en la vista kanban
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in self._fields['state'].selection]
    
    def _cron_set_done_surgery(self):
        surgeries = self.env['veterinary.surgery'].search([
            ('surgery_date', '<', fields.date.today()),
            ('state', '=', 'pending')
        ])
        surgeries.action_done()
        return True