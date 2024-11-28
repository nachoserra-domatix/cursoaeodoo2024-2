from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import timedelta

class VeterinaryAppointmentPetContact(models.TransientModel):
    _name = "veterinary.appointment.pet.contact"
    _description = "Veterinary appointmen pet contact"

    number=fields.Integer(string="number",required=True,default=1)
    pet_id=fields.Many2one('veterinary.pet',string="Pet",required=True)
    partner_id=fields.Many2one('res.partner',string="Contact",required=True)
    date= fields.Date(string="Date",required=True)


    def create_appointments(self):
       
        appointment_date = self.date
        created_appointments = []
        for i in range(self.number):
            appointment=self.env['veterinary.appointment'].create({
                'name':self.partner_id.name+" "+self.pet_id.name+" "+str(appointment_date),
                'partner_id': self.partner_id.id,
                'pet_id': self.pet_id.id,
                'date': appointment_date,
            })
            appointment_date += timedelta(days=30)
            created_appointments.append(appointment.id)
        
        return {
            
            'type':'ir.actions.act_window',
            'name':'Appointments created',
            'res_model':'veterinary.appointment',
            'view_mode':'tree,form,kanban',
            'domain': [('id', 'in', created_appointments)],
        }