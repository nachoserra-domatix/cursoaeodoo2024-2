from odoo import api, fields, models

class VeterinaryAppointmentStatesUpdateWizard(models.TransientModel):
    _name = 'veterinary.appointment.states.update.wizard'
    _description = 'Wizard to update veterinary appointment states'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')

    def update_states(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        if active_ids:
            records = self.env['veterinary.appointment'].browse(active_ids)
            records.write({'state': self.state})
        return {'type': 'ir.actions.act_window_close'}