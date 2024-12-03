from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError, UserError


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Veterinary Appointment'
    _order = 'date desc'
    # si hay sequence, no funciona _order

    name = fields.Char(string='Name')
    date = fields.Datetime(string='Date', required=True,
                           default=fields.Datetime.now)
    reason = fields.Text(string='Reason')
    solution = fields.Html(string='Solution')
    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='draft',
        group_expand='_group_expand_states',
        tracking=True
    )
    duration = fields.Float(string='Duration (minutes)',
                            help='Duration in minutes')
    sequence = fields.Integer(string='Sequence')
    urgency = fields.Boolean(string='Urgency')
    color = fields.Integer(string='Color', company_dependent=True)
    assigned = fields.Boolean(string='Assigned', default=False)
    # Many2one
    user_id = fields.Many2one('res.users', string='Responsible')
    partner_id = fields.Many2one('res.partner', string='Partner')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    company_id = fields.Many2one(
        'res.company', default=lambda self: self.env.company)
    # Many2many
    tag_ids = fields.Many2many(
        comodel_name='veterinary.appointment.tag', string='Tags')
    # One2many
    line_ids = fields.One2many(
        comodel_name='veterinary.appointment.line', inverse_name='appointment_id')
    # related fields
    # campo telèfono: a partir del campo partner_id; por defecto no se guarda en bd y es de solo lectura
    partner_phone = fields.Char(
        related='partner_id.phone', string='Partner Phone', store=True, readonly=False)
    partner_email = fields.Char(
        related='partner_id.email', string='Partner Email')
    # computed fields
    # por defecto no se guarada en bd
    # assigned = fields.Boolean(
    #     compute='_compute_assigned', inverse='_inverse_assigned', store=True)
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    # computed methods
    # marcar assigned si hay usuario
    # con @api.depends asignamos que dependa de un campo; si no se pone, se calculará a cada render de la vista
    # @api.depends('user_id')
    # def _compute_assigned(self):
    #     for record in self:
    #         record.assigned = bool(record.user_id)

    @api.depends('line_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(record.line_ids.mapped('subtotal'))

    # inverse methods
    # guardar usuario si marcamos assigned
    # def _inverse_assigned(self):
    #     for record in self:
    #         if record.assigned:
    #             record.user_id = self.env.user
    #         else:
    #             record.user_id = False

    # api constrains
    @api.constrains('duration')
    def check_duration(self):
        for record in self:
            if record.duration < 0:
                raise ValidationError(
                    _('The duration must be greater than 0')
                )

    # onchange
    @api.onchange('assigned')
    def _onchange_assigned(self):
        if self.assigned:
            self.user_id = self.env.user
        else:
            self.user_id = False

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_phone = self.partner_id.phone or self.partner_id.mobile
        else:
            self.partner_phone = False

    # methods
    def action_draft(self):
        for record in self:
            # pdb: punto de interrupción por consola odoo
            # import pdb;pdb.set_trace()
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'
            record.message_post(body="Appointment Done!",
                                message_type="notification")

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

    # overwrite create - sequence
    # con next_by_code: pasamos id de la sequence
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code(
            'veterinary.appointment')
        if self.env.context.get('followup_name'):
            vals['name'] = self.env.context.get(
                'name') + ' - ' + self.env.context.get('followup_name')
        res = super().create(vals)
        return res
