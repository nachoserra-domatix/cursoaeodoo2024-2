from odoo import models, fields, api, Command


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    date = fields.Datetime(string='Date', required=True,
                           default=fields.Datetime.now)
    reason = fields.Text(string='Reason')
    solution = fields.Html(string='Solution')
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='draft',
        group_expand='_group_expand_states'
    )
    duration = fields.Float(string='Duration (minutes)',
                            help='Duration in minutes')
    sequence = fields.Integer(string='Sequence')
    urgency = fields.Boolean(string='Urgency')
    color = fields.Integer(string='Color')
    # computed fields
    # por defecto no se guarada en bd
    assigned = fields.Boolean(
        compute='_compute_assigned', inverse='_inverse_assigned', store=True)

    # related fields
    user_id = fields.Many2one('res.users', string='Responsible')
    partner_id = fields.Many2one('res.partner', string='Partner')
    # campo telèfono: a partir del campo partner_id; por defecto no se guarda en bd y es de solo lectura
    partner_phone = fields.Char(
        related='partner_id.phone', string='Partner Phone', store=True, readonly=False)
    partner_email = fields.Char(
        related='partner_id.email', string='Partner Email')
    tag_ids = fields.Many2many(
        comodel_name='veterinary.appointment.tag', string="Tags")

    # computed methods
    # marcar assigned si hay usuario
    # con @api.depends asignamos que dependa de un campo; si no se pone, se calculará a cada render de la vista
    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    # inverse methods
    # guardar usuario si marcamos assigned
    def _inverse_assigned(self):
        for record in self:
            if record.assigned:
                record.user_id = self.env.user
            else:
                record.user_id = False

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

    # orm methods
    def create_tags_by_reason(self):
        tag_ids = self.env['veterinary.appointment.tag'].search(
            [('name', 'ilike', self.reason)])
        if tag_ids:
            self.tag_ids = [(6, 0, self.tag_ids.ids)]
        else:
            self.tag_ids = [(0, 0, {'name': self.reason})]
