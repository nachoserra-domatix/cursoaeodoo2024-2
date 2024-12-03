from odoo import models, fields, api, Command
from odoo.exceptions import ValidationError

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True, copy=False, default='New')
    partner_id = fields.Many2one('res.partner', string='Partner')
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    partner_phone = fields.Char(string='Phone')
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
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    sequence = fields.Integer(string='Sequence', default=10)
    urgency = fields.Boolean(string='Urgent')
    color = fields.Integer(string='Color', company_dependent=True)
    assigned = fields.Boolean(string='Assigned')
    tag_ids = fields.Many2many('veterinary.appointment.tag', string='Tags')
    line_ids = fields.One2many('veterinary.appointment.line', 'appointment_id', string='Lines')
    total = fields.Monetary(string='Total', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_unique', 'unique (name)', "The appointment name must be unique"),]
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('veterinary.appointment2')
        if self.env.context.get('followup_name'):
            vals['name'] = vals.get('name') + ' - ' + self.env.context.get('followup_name')
        res = super().create(vals)
        return res

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

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration < 0:
                raise ValidationError('The duration must be greater than zero')

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
        import pdb;pdb.set_trace()
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
            