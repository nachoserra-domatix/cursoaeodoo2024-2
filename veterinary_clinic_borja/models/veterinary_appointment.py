from odoo import fields, models, api, Command

class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # Name by defect is reason
    # _rec_name = "reason"

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one("res.partner", string="partner")
    partner_phone = fields.Char(related="partner_id.phone", string="Phone", store=True, readonly=False)
    partner_email = fields.Char(related="partner_id.email", string="Email")
    date = fields.Datetime(string="Date", required=True)
    reason = fields.Text(string="Reason", required=True)
    solution = fields.Html(string="Solution", translate=True)
    status = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status", group_expand="_group_expand_status")
    duration_minutes = fields.Integer(string="Duration", required=True, help="Duration in minutes")
    user_id = fields.Many2one("res.users", string="Responsible")
    sequence = fields.Integer(string="Sequence", default=10)
    urgency = fields.Boolean(string="Urgency")
    #color for the Kanban view
    color = fields.Integer(string="Color")
    assigned = fields.Boolean(string="Assigned", compute="_compute_assigned", inverse="_inverse_assigned", store=True)
    tag_ids = fields.Many2many("veterinary.appointment.tag", string="")
    line_ids = fields.One2many( "veterinary.appointment.line", "appointment_id", string="Lines")
    currency_id = fields.Many2one("res.currency", string="Currency", default=lambda self: self.env.company.currency_id)
    total = fields.Monetary(string="Total", currency_field='currency_id')
 

    def action_all_draft(self):
        self._set_all_status("draft")
    
    def action_all_done(self):
         self._set_all_status("done")

    def action_all_cancelled(self):
         self._set_all_status("cancelled")
    
    def action_all_other(self):
         self._set_all_status("other")

    def action_draft(self):
        self._set_status("draft")
    
    def action_done(self):
         if self.ensure_one():
               self.tag_ids = [(0,0,{"name": "done", "code": "done"})]
               self._set_status("done")

    def action_cancelled(self):
         self._set_status("cancelled")
    
    def action_other(self):
         self._set_status("other")
    
    def _set_status(self, status):
        self.status = status
    
    def _set_all_status(self, status):
        for record in self:
            record.status = status

     # in kanban view show all status colunns
    def _group_expand_status(self, status, domain, order):
          return [key for key , val in type(self).status.selection]
    
    # work with store=True in the declaration field
    @api.depends("user_id") 
    def _compute_assigned(self):
          for record in self:
               record.assigned = bool(record.user_id)

    def _inverse_assigned(self):
          for record in self:
               if record.assigned:
                    record.user_id = self.env.user
               else:
                     record.user_id = False
    def create_tags(self):
          tag_ids = self.env["veterinary.appointment.tag"].search([("name", "ilike", self.reason)])
          if tag_ids:
               tag_ids |= self.tag_ids # add the existents tag_ids without duplicates
               self.tag_ids = [Command.set(tag_ids.ids)]
               # self.tag_ids = [(6,0,self.tag_ids.ids)]
          else:
               self.tag_ids = [Command.create({"name": self.reason, "code": self.reason})]
               # self.tag_ids = [(0,0,{"name": self.reason, "code": self.reason})]

    