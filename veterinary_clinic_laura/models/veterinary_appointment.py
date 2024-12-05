from odoo import models, fields,api, Command
from odoo.exceptions import UserError, ValidationError, AccessDenied

class VeterinaryAppointment(models.Model):
   _name = "veterinary.appointment"
   _description = "Veterinary Appointment"

   _inherit=['mail.thread','mail.activity.mixin']
   _order= "date desc,id desc"
   
   def _group_expand_states(self, states, domain,order):
      return [key for key ,val in type(self).state.selection]

   name=fields.Char(string="Name",required=True,copy=False, default="New")
   partner_id=fields.Many2one('res.partner',string="Partner")
   partner_phone=fields.Char(string="Phone", related="partner_id.phone",store=True,readonly=False)
   partner_email=fields.Char(string="Email",related='partner_id.email',store=True,readonly=False)
   date = fields.Datetime(string='Date',required=True,help='Date of the appointment',default=fields.Datetime.now)
   reason = fields.Text(string='Reason',help='Reason for the appointment')
   solution=fields.Html(string="Solution",help="Solution for the problem")
   state= fields.Selection([
     ('draft','Draft'),
     ('done','Done'),
     ('cancelled','Cancelled'),
   ],default='draft', string='State', group_expand="_group_expand_states",tracking=True)
   duration=fields.Float(string='Duration')
   user_id = fields.Many2one('res.users',string="Responsible")
   urgency = fields.Boolean(string="Urgent")
   color= fields.Integer(string="Color",company_dependent=True)
   assigned=fields.Boolean(string="Assigned",store=True)
   tag_ids= fields.Many2many('veterinary.appointment.tag',string="Tags")
   lines_ids=fields.One2many('veterinary.appointment.line','appointment_id',string="Lines")
   total=fields.Float(string="Total", compute="_compute_total")
   pet_id=fields.Many2one('veterinary.pet',string="Pet")
   company_id=fields.Many2one('res.company',string="Company",default=lambda self: self.env.user.company_id)

   _sql_constraints=[
      ('name_unique', 'unique(name)','The appointment name must be unique'),
   ]
   
   @api.depends('color')
   def _compute_company(self):
      for record in self:
         if record.user_id:
            record.company_id = self.env.company

   @api.onchange('assigned')
   def _onchange_assigned(self):
      for record in self:
         if record.assigned:
            record.user_id=self.env.user
         else:
            record.user_id=False
   @api.onchange('partner_id')
   def _onchange_partner_id(self):
        if self.partner_id:
            self.partner_phone = self.partner_id.phone or self.partner_id.mobile
        else:
            self.partner_phone = False

   @api.model
   def create(self,vals):
      vals["name"]=self.env['ir.sequence'].next_by_code('veterinary.appointment')
      if self.env.context.get('follow_up_name'):
         vals["name"]= vals["name"]+" "+self.env.context.get('follow_up_name')
      res=super().create(vals)
      return res
   
   @api.constrains('duration')
   def _check_duration(self):
      for record in self:
         if record.duration<0:
            raise ValidationError('The duration must be positive')
   
   def _compute_total(self):
      for record in self:
         record.total= sum(record.lines_ids.mapped("subtotal"))
   
   
   def _inverse_assigned(self):
      for record in self:
         if record.assigned:
            record.user_id=self.env.user
         else:
            record.user_id=False
   
   @api.depends('user_id')
   def _compute_assigned(self):
      for record in self:
         record.assigned= bool(record.user_id)

   def action_draft(self):
      for record in self:
        #import pdb;pdb.set_trace()
        record.state = 'draft'

   def action_done(self):
      for record in self:
        record.state = 'done'
        record.message_post(body='Appointment done',message_type="notification")

   def action_cancel(self):
      for record in self:
         record.state = 'cancelled'

   def create_tags(self):
      
      tag_ids = self.env['veterinary.appointment.tag'].search([('name','ilike',self.reason)])
      #tag_ids |= self.tag_ids
      if tag_ids:
         self.tag_ids=[Command.set(tag_ids.ids)]
      else:
         self.tag_ids=[Command.create({'name':self.reason})]