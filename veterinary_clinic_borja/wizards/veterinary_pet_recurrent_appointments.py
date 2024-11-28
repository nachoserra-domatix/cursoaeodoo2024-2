from odoo import fields, models, tools


class VeterinaryPetRecurrentAppointments(models.TransientModel):
    _name = "veterinary.pet.recurrent.appointments"
    _description = "Vaterinary Pet Recurrent Appointments"

    appointments = fields.Integer(string="Number of Appointments")
    partner_id = fields.Many2one("res.partner", string="partner")

    def create_n_appointments(self):
        active_ids = self.env.context.get("active_ids")
        pet = self.env["veterinary.pet"].browse(active_ids)
        appointment_date = tools.date_utils.add(fields.Datetime.now(), months=1)
        for appointment in range(self.appointments):
            self.env["veterinary.appointment"].create(
                {
                    "name": f"wizard appointment {appointment+1}",
                    "partner_id": self.partner_id.id,
                    "date": appointment_date,
                    "reason": f"Reason wizard appointment {appointment+1}",
                    "pet_id": pet.id,
                    "duration_minutes": 0,
                }
            )
            appointment_date = tools.date_utils.add(appointment_date, months=1)
