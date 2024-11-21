from odoo import models, fields

class AdoptionState(models.Model):
    _name = 'veterinary.adoption.state'
    _description = 'Adoption state'

    name = fields.Char('Name', required=True)
    adopted = fields.Boolean(string='Adopted')
