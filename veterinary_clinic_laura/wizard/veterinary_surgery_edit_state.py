from odoo import api, fields, models, _
from odoo.exceptions import UserError


class VeterinarySurgeryEditState(models.TransientModel):
    _name = "veterinary.surgery.edit.state"
    _description = "Veterinary surgery edit state"

    state= fields.Selection([
        ('wait','Wait'),
        ('doing','Doing'),
        ('finish','Finish'),
    ],default='wait', string='State')

    def mass_edit_state(self):
        active_ids=self.env.context.get('active_ids',False)
        if not active_ids:
            active_ids=self.env['veterinary.surgery'].search([]).ids
        surgeries= self.env['veterinary.surgery'].browse(active_ids)
        surgeries.write({'state':self.state})