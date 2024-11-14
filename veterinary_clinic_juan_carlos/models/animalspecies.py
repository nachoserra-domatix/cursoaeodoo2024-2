from odoo import models, fields

class AnimalSpecies(models.Model):
    _name = "veterinary.animalspecies"
    _description = "Veterinary animalspecies"

    name = fields.Char(string="Name", required=True)
    