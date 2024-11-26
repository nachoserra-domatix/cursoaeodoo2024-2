from odoo import models, fields, api

class VeterinarySurgeryEditState(models.TransientModel):
    _name = 'veterinary.surgery.edit.state'
    _description = 'Veterinary surgery Edit State'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], default='done', string='State')

    def mass_edit_state(self):
        active_ids = self.env.context.get('active_ids', False)
        if not active_ids:
            active_ids = self.env['veterinary.surgery'].search([]).ids
        surgeries = self.env['veterinary.surgery'].browse(active_ids)
        surgeries.write({'state': self.state})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Ventana nueva',
            'res_model': 'veterinary.surgery',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', surgeries.ids)],
        }