from odoo import models, fields, api

class VeterinarySurgeryEditState(models.TransientModel):
    _name = 'veterinary.surgery.edit.state'
    _description = 'Veterinary Surgery Edit State'


    surgery_state = fields.Selection([
        ('pending', 'Pending'),
        ('procces', 'In Procces'),
        ('done', 'Done')
    ], default='pending', string='State')


    def mass_edit_state(self):        
        active_ids = self.env.context.get('active_ids')
        if not active_ids:
            active_ids = self.env['veterinary.surgery'].search([]).ids
        surgeries = self.env['veterinary.surgery'].browse(active_ids)
        surgeries.write({'surgery_state': self.surgery_state})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Surgerys Changed',
            'view_mode': 'tree',
            'res_model': 'veterinary.surgery',            
            'domain': [('id', '=', surgeries.ids)],
        } # Permite abrir una vista de arbol con los registros seleccionados que se han cambiado