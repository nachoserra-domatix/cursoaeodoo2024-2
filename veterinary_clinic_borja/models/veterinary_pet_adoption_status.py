from odoo import fields, models

class VeterinaryPetAdoptionStatus(models.Model):
   _name = "veterinary.pet.adoption.status"
   _description = "Veterinary Pet Adoption Status"

   name = fields.Char(string="Name", required=True, help="Name of the pet adoption status")
   is_adopted = fields.Boolean(string="Adopted")