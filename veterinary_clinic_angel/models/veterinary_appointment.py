from odoo import models, fields, api, Command
from odoo.exceptions import ValidationError

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    partner_phone = fields.Char(string='Phone', readonly=False, store=True)
    partner_email = fields.Char(string='Email', related='partner_id.email', store=True)
    reason = fields.Char(string='Reason', required=True)
    solution = fields.Html(string='Solution', help='Solution of the appointment')
    date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft', group_expand='_group_expand_states')
    duration = fields.Float(string='Duration')
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    sequence = fields.Integer(string='Sequence', default=10)
    urgency = fields.Boolean(string='Urgent')
    color = fields.Integer(string='Color')
    tag_ids = fields.Many2many('veterinary.appointment.tag', string='Tags')
    line_ids = fields.One2many('veterinary.appointment.line', 'appointment_id',string='Lines')
    total = fields.Monetary(string='Total', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    assigned = fields.Boolean(string='Assigned', store=True)
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name of the appointment must be unique')
    ]

    @api.onchange('assigned')
    def _onchange_assigned(self):
        if self.assigned:
            self.user_id = self.env.user

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_phone = self.partner_id.phone

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration <= 0:
                raise ValidationError('The duration must be greater than zero')

    @api.depends('line_ids.price_subtotal')
    def _compute_total(self):
        for appointment in self:
            appointment.total = sum(line.price_subtotal for line in appointment.line_ids)


    @api.model
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'

    def action_create_tags(self):
        tag_ids = self.env['veterinary.appointment.tag'].search([('name', 'ilike', self.reason)])
        if tag_ids:
            self.tag_ids = [Command.set(tag_ids.ids)]
        else:
            self.tag_ids = [Command.create({'name': self.reason})]