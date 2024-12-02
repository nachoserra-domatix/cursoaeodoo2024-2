from odoo import models, fields, api


class VeterinaryVeterinarian(models.Model):
    _name = 'veterinary.veterinarian'
    _description = 'Veterinary Veterinarian'
    # herencia por delegación
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', string='Partner',
                                 required=True, ondelete='restrict')
    license_number = fields.Char(string='License Number')
    speciality = fields.Char(string='Speciality')
