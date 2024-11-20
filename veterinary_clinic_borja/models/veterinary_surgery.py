from odoo import fields, models

class VeterinarySurgery(models.Model):
    _name = "veterinary.surgery"
    _description = "Veterinary Surgery"

    name = fields.Char(string="Name", required=True, help="Name of the surgery")
    pet_id = fields.Many2one("veterinary.pet", string="Pet")
    employee_id = fields.Many2one("hr.employee", string="Responsible")
    surgery_date = fields.Date(string="Date", help="Date of the surgery")
    status = fields.Selection([
        ("draft", "Draft"),
        ("in_progress", "In progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status", group_expand="_group_expand_status")
    #color for the Kanban view
    color = fields.Integer(string="Color")
    action_ids = fields.One2many( "veterinary.surgery.action", "surgery_id", string="Actions")

    def action_draft(self):
        self._set_status("draft")

    def action_done(self):
        self._set_status("done")

    def action_in_progress(self):
        self._set_status("in_progress")

    def action_cancelled(self):
        self._set_status("cancelled")

    def action_other(self):
        self._set_status("other")

    def _set_status(self, status):
        self.status = status
    
    # in kanban view show all status colunns
    def _group_expand_status(self, status, domain, order):
          return [key for key , val in type(self).status.selection]
