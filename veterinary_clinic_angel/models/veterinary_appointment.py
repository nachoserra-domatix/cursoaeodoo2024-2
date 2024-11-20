from odoo import models, fields, api, Command

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    partner_phone = fields.Char(string='Phone', related='partner_id.phone', readonly=False, store=True)
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
    user_id = fields.Many2one('res.users', string='Responsible')
    sequence = fields.Integer(string='Sequence', default=10)
    urgency = fields.Boolean(string='Urgent')
    color = fields.Integer(string='Color')
    tag_ids = fields.Many2many('veterinary.appointment.tag', string='Tags')
    line_ids = fields.One2many('veterinary.appointment.line', 'appointment_id',string='Lines')


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