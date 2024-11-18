from odoo import models, fields


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    date = fields.Datetime(string='Date', required=True, default=fields.Datetime.now)
    reason = fields.Text(string='Reason')
    solution = fields.Html(string='Solution')
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='draft',
        group_expand='_group_expand_states'
    )
    duration = fields.Float(string='Duration (minutes)', help='Duration in minutes')
    user_id = fields.Many2one('res.users', string='Responsible')
    sequence = fields.Integer(string='Sequence')
    urgency = fields.Boolean(string='Urgency')
    color = fields.Integer(string='Color')

    # methods
    def action_draft(self):
      for record in self:
         # pdb: punto de interrupción por consola odoo
         # import pdb;pdb.set_trace()
         record.state = 'draft'

    def action_done(self):
        for record in self:
           record.state = 'done'

    def action_cancelled(self):
        for record in self:
           record.state = 'cancelled'

    # método odoo para forzar que salgan todos los estados en la vista kanban
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in self._fields['state'].selection]