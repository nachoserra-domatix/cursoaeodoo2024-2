from odoo import fields, models, tools


class VeterinaryPetRecurrentAppointments(models.TransientModel):
    _name = "veterinary.pet.recurrent.appointments"
    _description = "Vaterinary Pet Recurrent Appointments"

    appointments = fields.Integer(string="Number of Appointments", default=1)
    initial_date = fields.Datetime(
        string="Initial Date",
        required=True,
        default=tools.date_utils.add(fields.Datetime.now(), months=1),
    )
    partner_id = fields.Many2one("res.partner", string="partner")

    def create_n_appointments(self):
        active_ids = self.env.context.get("active_ids")
        pet = self.env["veterinary.pet"].browse(active_ids)
        appointment_date = self.initial_date
        created_appointments = self.env["veterinary.appointment"]
        for n_appointment in range(self.appointments):
            appointment = {
                "name": f"wizard appointment {n_appointment+1} - {pet.name} - {self.partner_id.name}",
                "partner_id": self.partner_id.id,
                "date": appointment_date,
                "reason": f"Reason wizard appointment {n_appointment+1}",
                "pet_id": pet.id,
                "duration_minutes": 0,
            }
            created_appointments |= (
                self.env["veterinary.appointment"]
                .with_context(follow_up=appointment.name)
                .create(appointment)
            )
            appointment_date = tools.date_utils.add(appointment_date, months=1)
        return {
            "type": "ir.actions.act_window",
            "name": "Ventana Nueva",
            "res_model": "veterinary.appointment",
            "view_mode": "tree,form",
            "domain": [("id", "in", created_appointments.ids)],
        }
