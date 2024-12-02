from odoo import models, fields, api
from datetime import timedelta

class VeterinaryGenerateAppointmentWizard(models.TransientModel):
    _name = 'veterinary.generate.appointment.wizard'
    _description = 'Veterinary Generate Appointment Wizard'

    
    partner_id = fields.Many2one('res.partner', string='Partner')
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    date = fields.Date(string='Date')
    appointment_count = fields.Integer(string='Appointment Count', default=1)

    def generate_appointments(self):
        date = self.date
        appointments = self.env['veterinary.appointment']
        for i in range(self.appointment_count):
            vals = {
                'partner_id': self.partner_id.id,
                'pet_id': self.pet_id.id,
                'date': date,
                'name': f'Followup of {self.pet_id.name} {i + 1}',
                'reason': 'Followup'
            }
            date = date + timedelta(days=31)
            appointments |= self.env['veterinary.appointment'].with_context(followup_name=vals.get('name')).create(vals)
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Followup Appointmets',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', appointments.ids)],
        }