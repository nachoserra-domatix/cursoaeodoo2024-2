from odoo import models, fields, api, Command

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'
    #_rec_name = 'reason' # Permite establecer el campo que va actuar como name cuando el campo name no exista 

    name = fields.Char(string='Name', required=True,)
    partner_id = fields.Many2one('res.partner', string='Partner')
    pet_id = fields.Many2one('veterinary.pet', string='Pet', help='Pet of the appointment')
    partner_phone = fields.Char(string='Phone')
    partner_email = fields.Char(string='Email', related='partner_id.email', store=True, readonly=False)
    date = fields.Datetime(string='Date', required=True, default =fields.Datetime.now, help='Date of the appointment')
    reason = fields.Text(string='Reason', help='Description of the appointment')
    solution = fields.Html(string='Solution', help='Solution of the appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft', string='State', help='State of the appointment', group_expand = '_group_expand_states')

    duration = fields.Float(string='Duration', help='Duration of the appointment')
    user_id = fields.Many2one('res.users', string='Responsible', help='Veterinarian in charge of the appointment', default=lambda self: self.env.user)
    sequence = fields.Integer(string='Sequence', default = 10)
    urgency = fields.Boolean(string='Urgent', help='Urgent appointment')
    color = fields.Integer(string='Color')
    assigned = fields.Boolean(string='Assigned', help='Assigned appointment', compute='_compute_assigned', inverse='_inverse_assigned', store=True)
    tag_ids = fields.Many2many('veterinary.appointment.tag', string='Tags', help='Tags of the appointment')
    line_ids = fields.One2many('veterinary.appointment.line', 'appointment_id', string='Lines', help='Lines of the appointment')
    total = fields.Float(string='Total', compute='_compute_total')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The appointment name must be unique')
    ]

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

    @api.constrains('duration')
    def _check_duration(self):      
        for record in self:
            if record.duration <= 0:
                raise models.ValidationError('Duration must be greater than zero')
            
    
            
    def _compute_total(self):
        for record in self:
            record.total = sum(line.subtotal for line in record.line_ids)

    def _inverse_assigned(self):
        for record in self:
            if record.assigned:
                record.user_id = self.env.user
            else:
                record.user_id = False

    def action_draft(self):
        for record in self:
            record.state = 'draft'   

    def action_done(self):
        for record in self:
            record.state = 'done'
        
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'

    def _group_expand_states(self,states,domian,order):
        return [key for key, val in type(self).state.selection]

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
          
            record.assigned = bool(record.user_id)

    def create_tags(self):
        tag_ids = self.env['veterinary.appointment.tag'].search([('name', 'ilike', self.reason)])
        if tag_ids:
            self.tag_ids = [Command.set(tag_ids.ids)]
            #self.tag_ids = [(6, 0, self.tag_ids.ids)]
        else:
            self.tag_ids=[Command.create({'name': self.reason})]
            #self.tag_ids = [(0, 0, self.tag_ids.ids)]