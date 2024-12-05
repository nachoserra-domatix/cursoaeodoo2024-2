
from odoo import models, fields, api
import random
import string
from datetime import date
from odoo.exceptions import UserError, ValidationError, AccessDenied

class ResPartner(models.Model):
    _inherit="res.partner"

    
    pet_count=fields.Integer(string="Pet Count",compute="_compute_pet_count")
    pet_ids=fields.One2many('veterinary.pet','partner_id',string="Pets")
 
    def _compute_pet_count(self):
      for record in self:
         record.pet_count= len(record.pet_ids)
    
    
    def action_view_res_partner_pets(self):
      return{
         'type':'ir.actions.act_window',
         'name':'Contact Pets',
         'res_model':'veterinary.pet',
         'view_mode':'tree,form',
         'domain':[('partner_id','=',self.id)]

      }