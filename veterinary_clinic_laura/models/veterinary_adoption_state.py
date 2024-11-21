from odoo import models, fields, api
import random
import string

class VeterinaryAdoptionState(models.Model):
   _name = "veterinary.adoption.state"
   _description = "Veterinary Adoption State"

   name = fields.Char(string='Name',required=True,help='Name of the pet')
   adopted= fields.Boolean(string="Adopted")
   