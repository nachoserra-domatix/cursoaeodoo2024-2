from odoo import models, fields, api

class VeterinarySurgeriesEditState(models.TransientModel):
    _name = "veterinary.surgeries.edit.state"
    _description = "vete edit"
    
    surgerie_date_state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string="Status", default="scheduled", help="Current status of the surgery")

    def mass_edit_state(self):
        active_ids = self.env.context.get("active_ids")
        surgeriess = self.env["veterinary.surgeries"].browse(active_ids)
        surgeriess.write({"surgerie_date_state": self.surgerie_date_state})