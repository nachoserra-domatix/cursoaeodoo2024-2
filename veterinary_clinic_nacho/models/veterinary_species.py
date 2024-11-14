from odoo import fields, models


class VeterinarySpecies(models.Model):
    _name = 'veterinary.species'
    _description = 'Veterinary Species'

    name = fields.Char(string='Name', required=True, help='Name of the species')