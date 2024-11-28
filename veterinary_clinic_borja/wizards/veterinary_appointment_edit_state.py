from odoo import fields, models


class VeterinaryAppointmentEditState(models.TransientModel):
    _name = "veterinary.appointment.edit.state"
    _description = "Veterinary Appointment Edit State"

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
            ("other", "Other"),
        ],
        default="draft",
        string="State",
    )

    def mass_edit_state(self):
        active_ids = self.env.context.get("active_ids")
        appointments = self.env["veterinary.appointment"].browse(active_ids)
        appointments.write({"status": self.state})
