from odoo import fields, models


class VeterinarySurgeryEditStatus(models.TransientModel):
    _name = "veterinary.surgery.edit.status"
    _description = "Veterinary Surgery Edit Status"

    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
            ("other", "Other"),
        ],
        default="draft",
        string="Status",
    )

    def mass_edit_status(self):
        active_ids = self.env.context.get("active_ids")
        if not active_ids:
            active_ids = self.env["veterinary.appointment"].search([])
        surgeries = self.env["veterinary.surgery"].browse(active_ids)
        surgeries.write({"status": self.status})
        context = dict(self.env.context)
        context.update({"default_status": "draft"})
        return {
            "type": "ir.actions.act_window",
            "name": "Ventana Nueva",
            "res_model": "veterinary.surgery.edit.status",
            "view_mode": "form",
            "target": "new",
            "context": context,
        }
