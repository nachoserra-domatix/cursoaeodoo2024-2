from odoo import api, fields, models

class VeterinarySurgeryStatesUpdateWizard(models.TransientModel):
    _name = 'veterinary.surgery.states.update.wizard'
    _description = 'Wizard to update veterinary surgery states'

    state = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='scheduled')

    def update_states(self):
        self.ensure_one()
        active_ids = self.env.context.get('active_ids')
        if active_ids:
            records = self.env['veterinary.surgery'].browse(active_ids)
            records.write({'state': self.state})
        return {'type': 'ir.actions.act_window_close'}