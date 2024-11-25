from odoo import fields, models, api
from odoo.exceptions import ValidationError

class VeterinaryPetAdoption(models.Model):
   _name = "veterinary.pet.adoption"
   _description = "Veterinary Pet Adoption"

   name = fields.Char(string="Name", required=True, help="Name of the pet adoption")
   shelter_entry = fields.Date(string="Shelter entry date", help="Shelter entry date of the pet")
   adoption_date = fields.Date(string="Adoption date")
   pet_id = fields.Many2one("veterinary.pet", string="Pet")
   partner_id = fields.Many2one("res.partner", string="partner")
   status_id = fields.Many2one("veterinary.pet.adoption.status", string="Adoption status", group_expand="_group_expand_status")
   user_id = fields.Many2one("res.users", string="Responsible")
   shelter_days = fields.Integer(string="Days in the shelter", default=1)
   notes = fields.Text(string="Notes")
   currency_id = fields.Many2one("res.currency", string="Currency", default=lambda self: self.env.company.currency_id)
   adoption_fee = fields.Monetary(string="Adoption fee", currency_field='currency_id')
   #color for the Kanban view
   color = fields.Integer(string="Color")
   avatar_pet = fields.Image(related="pet_id.avatar")

   def _group_expand_status(self, status, domain, order):
      return status.search([])
   
   @api.constrains("adoption_date", "shelter_entry")
   def _check_dates(self):
      for rec in self:
         if rec.shelter_entry > rec.adoption_date:
            raise ValidationError("shelter_entry not valid")
            


