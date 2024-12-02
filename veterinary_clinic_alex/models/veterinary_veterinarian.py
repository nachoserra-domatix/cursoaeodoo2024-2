from odoo import models, fields, api

class VeterinaryVeterinarian(models.Model):
    _name = 'veterinary.veterinarian'
    _description = 'Veterinary Veterinarian'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict')
    license_number = fields.Char(string='License Number')
    specialty = fields.Char(string='Specialty')
    