from odoo import fields, models

class VeterinaryAppointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # Name by defect is reason
    # _rec_name = "reason"

    name = fields.Char(string="Name", required=True)
    date = fields.Datetime(string="Date", required=True)
    reason = fields.Text(string="Reason", required=True)
    solution = fields.Html(string="Solution", translate=True)
    status = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status")
    duration_minutes = fields.Integer(string="Duration", required=True, help="Duration in minutes")
    user_id = fields.Many2one("res.users", string="Responsible")
    sequence = fields.Integer(string="Sequence", default=10)
    urgency = fields.Boolean(string="Urgency")

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