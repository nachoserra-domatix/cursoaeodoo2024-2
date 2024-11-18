from odoo import models, fields

class VeterinaryAppointment(models.Model):
   _name = "veterinary.appointment"
   _description = "Veterinary Appointment"
   
   def _group_expand_states(self, states, domain,order):
      return [key for key ,val in type(self).state.selection]

   name=fields.Char(string="Name",required=True)
   date = fields.Datetime(string='Date',required=True,help='Date of the appointment',default=fields.Datetime.now)
   reason = fields.Text(string='Reason',help='Reason for the appointment')
   solution=fields.Html(string="Solution",help="Solution for the problem")
   state= fields.Selection([
     ('draft','Draft'),
     ('done','Done'),
     ('cancelled','Cancelled'),
   ],default='draft', string='State', group_expand="_group_expand_states")
   duration=fields.Float(string='Duration')
   user_id = fields.Many2one('res.users',string="Responsible")
   sequence = fields.Integer(string="Sequence",default=10)
   urgency = fields.Boolean(string="Urgent")
   color= fields.Integer(string="Color")

   def action_draft(self):
      for record in self:
        #import pdb;pdb.set_trace()
        record.state = 'draft'

   def action_done(self):
      for record in self:
        record.state = 'done'
   def action_cancel(self):
      for record in self:
         record.state = 'cancelled'

  
  
    