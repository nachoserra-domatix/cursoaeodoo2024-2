from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class VeterinaryAppointmentCreateWizard(models.TransientModel):
    _name = 'veterinary.appointment.create.wizard'
    _description = 'Wizard to create veterinary appointments'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    number_of_appointments = fields.Integer(string='Number of Appointments', default=1)

    @api.constrains('number_of_appointments')
    def _check_number_of_appointments(self):
        for record in self:
            if record.number_of_appointments <= 0:
                raise ValidationError('The number of appointments must be greater than zero')

    def create_appointments(self):
        self.ensure_one()

        for i in range(self.number_of_appointments):
            appointment_vals = {
                'pet_id': self.pet_id.id,
                'partner_id': self.partner_id.id,
                'date': self.date + relativedelta(months=i),
            }
            self.env['veterinary.appointment'].create(appointment_vals)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'target': 'current',
        }