from odoo import models, fields

class VeterinaryAdoptionState(models.Model):
    _name= 'veterinary.adoption.state'
    _description = 'Veterinary Adoption State'

    name = fields.Char(string='Name')
    is_adopted = fields.Boolean(string='Is Adopted')
