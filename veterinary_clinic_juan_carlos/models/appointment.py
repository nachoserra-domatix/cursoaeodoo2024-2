from odoo import models, fields

class Appointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # _rec_name = "reason" #actua como nombre

    name = fields.Char(string="Name", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", help="Date and time", default=fields.Datetime.now)
    solution = fields.Html(string='Solution', help='Solution to the problem')
    reason = fields.Text(string="Reason for Appointment", help="reason")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default="draft", help="current status of the appointment")
    duration = fields.Float(string="Duration (minutes)", help="Duration minutes")
    user_id = fields.Many2one("res.users", string="Responsible")
    sequence = fields.Integer(string="Sequence", default=10)
    urgency = fields.Boolean(string="Urgent")



    def action_draft(self):
        for record in self:
            record.state = "draft"
            # import pdb;pdb.set_trace()
    

    def action_done(self):
        for record in self:
            record.state = "done"


    def action_cancelled(self):
        for record in self:
            record.state = "cancelled"


    # def action_draft(self):
    #     self.state = "draft"

    # def action_all_draft(self):
    #     appointments = self.search([])
    #     appointments.action_draft()