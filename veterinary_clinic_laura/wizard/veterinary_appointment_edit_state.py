from odoo import api, fields, models, _
from odoo.exceptions import UserError


class VeterinaryAppointmentEditState(models.TransientModel):
    _name = "veterinary.appointment.edit.state"
    _description = "Veterinary appointmen edit state"

    state= fields.Selection([
     ('draft','Draft'),
     ('done','Done'),
     ('cancelled','Cancelled'),
   ],default='draft', string='State')

    def mass_edit_state(self):
        active_ids=self.env.context.get('active_ids')
        appointments= self.env['veterinary.appointment'].browse(active_ids)
        appointments.write({'state':self.state})