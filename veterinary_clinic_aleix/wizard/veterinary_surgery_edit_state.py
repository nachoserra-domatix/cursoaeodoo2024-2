from odoo import models, fields, api


class VeterinarySurgeryEditState(models.TransientModel):
    _name = 'veterinary.surgery.edit.state'
    _description = 'Veterinary Surgery Edit State'

    state = fields.Selection(
        selection=[('pending', 'Pending'), ('in_progress', 'In progress'), (
            'done', 'Done'), ('cancelled', 'Cancelled')],
        string='State',
        default='done'
    )

    def mass_edit_state(self):
        active_ids = self.env.context.get('active_ids', False)
        # si por contexto no tiene 'active_ids', buscalas todas
        if not active_ids:
            active_ids = self.env['veterinary.surgery'].search([]).ids
        appointments = self.env['veterinary.surgery'].browse(active_ids)
        appointments.write({'state': self.state})
