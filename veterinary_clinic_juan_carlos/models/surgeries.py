from odoo import fields, models

class Surgeries(models.Model):
    _name = "veterinary.surgeries"
    _description = "Veterinary Surgeries"

    name = fields.Char(string="Name", required=True, help="Name of the surgerie")
    pet_id = fields.Many2one('veterinary.pet', string="Pet")
    doctor = fields.Many2one('hr.employee', string="doctor")
    surgerie_date = fields.Datetime(string="Surgerie Date", help="Date and time")
    surgerie_date_state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string="Status", default="scheduled", help="Current status of the surgery")
    color = fields.Integer(string="Color")
    action_ids = fields.One2many("veterinary.surgeries.action","surgery_id", string="Surgery ids")

    def action_scheduled(self):
        for record in self:
            record.surgerie_date_state = "scheduled"
    
    def action_in_progress(self):
        for record in self:
            record.surgerie_date_state = "in_progress"

    def action_completed(self):
        for record in self:
            record.surgerie_date_state = "completed"

    def _cron_chek_draft_date(self):
        draft_surgeries = self.search([("surgerie_date_state", "=", "scheduled")])
        for surgery in draft_surgeries:
            if surgery.surgerie_date < fields.datetime.now():
                surgery.surgerie_date_state = "completed"