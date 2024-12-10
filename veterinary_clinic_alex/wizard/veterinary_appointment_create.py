from odoo import models, fields, api
from datetime import  timedelta

class VeterinaryAppointmentCreate(models.TransientModel):
    _name = 'veterinary.appointment.create'
    _description = 'Veterinary Appointment Create'

    name = fields.Char(string='Name', default='Cita')
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    partner_id = fields.Many2one('res.partner', string='Owner')
    date = fields.Date(string='Date')
    number = fields.Integer(string='Number', default=1)


    def create_appointments(self):    
        name = self.name
        appointments = self.env['veterinary.appointment']
        for record in range(self.number):
            name = self.name + '#' + str(record+1)
            
            vals = {
                'name': 'Followup of' + name, 
                'pet_id': self.pet_id.id,
                'partner_id': self.partner_id.id,
                'date': self.date,
                'state': 'draft',
                'reason': 'Followup'
            }
     
            self.date = self.date + timedelta(days=self.number) 
            appointments |= self.env['veterinary.appointment'].with_context(followup_name=vals.get('name')).create(vals) 
            #necesario completar el código para que se creen las citas           
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurance History',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form',
            'domain': [('id', '=' , appointments.ids)],
        }
    