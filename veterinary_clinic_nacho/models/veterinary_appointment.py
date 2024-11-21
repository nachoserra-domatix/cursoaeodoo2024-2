from odoo import models, fields, api, Command


class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    partner_phone = fields.Char(string='Phone', related='partner_id.phone', store=True, readonly=False)
    partner_email = fields.Char(string='Email', related='partner_id.email', store=True, readonly=False)
    date = fields.Datetime(string='Date', required=True, help='Date of the appointment', default=fields.Datetime.now)
    reason = fields.Text(string='Reason', help='Reason for the appointment')
    solution = fields.Html(string='Solution', help='Solution to the problem')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft', string='State', group_expand='_group_expand_states')
    duration = fields.Float(string='Duration')
    user_id = fields.Many2one('res.users', string='Responsible')
    sequence = fields.Integer(string='Sequence', default=10)
    urgency = fields.Boolean(string='Urgent')
    color = fields.Integer(string='Color')
    assigned = fields.Boolean(string='Assigned', compute='_compute_assigned', inverse='_inverse_assigned')
    tag_ids = fields.Many2many('veterinary.appointment.tag', string='Tags')
    line_ids = fields.One2many('veterinary.appointment.line', 'appointment_id', string='Lines')
    total = fields.Monetary(string='Total', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    @api.depends('line_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total = sum(record.line_ids.mapped('subtotal'))

    def _inverse_assigned(self):
        for record in self:
            if record.assigned:
                record.user_id = self.env.user
            else:
                record.user_id = False

    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
    
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    
    def create_tags(self):
        tag_ids = self.env['veterinary.appointment.tag'].search([('name','ilike', self.reason)])
        # Si quisiera añadir las etiquetas existentes podría usar el siguiente operador:
        # tag_ids |= self.tag_ids
        if tag_ids:
            self.tag_ids = [Command.set(tag_ids.ids)]
            #self.tag_ids = [(6, 0, self.tag_ids.ids)]
        else:
            self.tag_ids = [Command.create({'name': self.reason})]
            #self.tag_ids = [(0,0, {'name': self.reason})]
            