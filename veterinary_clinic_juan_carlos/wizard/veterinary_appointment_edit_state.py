from odoo import models, fields, api

class VeterinaryAppointmentEditState(models.TransientModel):
    _name = "veterinary.appointment.edit.state"
    _description = "vete edit"
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string="Status", default="draft", help="current status of the appointment")

    def mass_edit_state(self):
        active_ids = self.env.context.get("active_ids")
        appointments = self.env["veterinary.appointment"].browse(active_ids)
        appointments.write({"state": self.state})