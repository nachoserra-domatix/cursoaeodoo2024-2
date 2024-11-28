from odoo import _, models, fields, api
from odoo.tools import date_utils
from odoo.exceptions import ValidationError, UserError


class VeterinaryAppointmentMassGeneration(models.TransientModel):
    _name = 'veterinary.appointment.mass.generation'
    _description = 'Veterinary Appointment Mass Generation'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True)
    number = fields.Integer(string='Number of appointments', required=True)

    # api constrains
    @api.constrains('number')
    def check_number(self):
        if self.number <= 0:
            raise ValidationError(
                _('The number must be greater than 0')
            )

    def appointment_mass_generation(self):
        appointments = self.env['veterinary.appointment']
        for i in range(self.number):
            appointment = self.env['veterinary.appointment']
            date = date_utils.add(fields.date.today(), months=i+1)
            vals = {}
            vals['pet_id'] = self.pet_id.id
            vals['partner_id'] = self.partner_id.id
            vals['date'] = date
            vals['name'] = f'Appointment #{i+1} - {self.pet_id.name} - {str(date)}'
            # creamos la cita, y la acumulamos en lista
            appointments |= appointment.create(vals)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Followup appointments',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', appointments.ids)]
        }
