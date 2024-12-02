from odoo import models, fields
from datetime import timedelta

class VeterinaryAppointmentCreateFollow(models.TransientModel):
    _name = "veterinary.appointment.create.follow"
    _description = "Create Follow"
    
    partner_id = fields.Many2one("res.partner", string="Partner")
    appointment_date = fields.Datetime(string="Appointment Date", help="Date and time", default=fields.Datetime.now)
    pet_id = fields.Many2one("veterinary.pet", string="pet")
    follow_up_count = fields.Integer(string="Number of Follow-ups", default=1)

    def create_follow_appointments(self):
        """Create follow-up appointments for a pet and contact."""
        appointment = self.env['veterinary.appointment']
        follow_up_interval = 30
        for wizard in self:
            for i in range(wizard.follow_up_count):
                follow_up_date = wizard.appointment_date + timedelta(days=follow_up_interval * i)
                name = f"{wizard.pet_id.name} - Follow {i + 1}"

                appointment.with_context(follow_up=name).create({
                'name': name,
                'partner_id': wizard.partner_id.id,
                'pet_id': wizard.pet_id.id,
                'appointment_date': follow_up_date,
            })