from odoo import fields,models,api

class VeterinaryAdoptionStage(models.Model):
    _name = 'veterinary.adoption.stage'
    _description = 'Veterinary Adoption Stage'

    name = fields.Char(string='Name', required=True)
    adopted = fields.Boolean(string='Adopted')