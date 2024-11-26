from odoo import fields, models

class VeterinarySurgeryEditStatus(models.TransientModel):
    _name="veterinary.surgery.edit.status"
    _description="Veterinary Surgery Edit Status"

    status = fields.Selection([
       ("draft", "Draft"),
        ("in_progress", "In progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
        ("other", "Other")   
    ], default="draft", string="Status")

    def mass_edit_status(self):
        active_ids = self.env.context.get("active_ids")
        surgeries = self.env["veterinary.surgery"].browse(active_ids)
        surgeries.write({"status": self.status})