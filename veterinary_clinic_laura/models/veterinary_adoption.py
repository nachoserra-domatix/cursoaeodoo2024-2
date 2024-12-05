from odoo import models, fields, api
import random
import string
from datetime import date
from odoo.exceptions import UserError, ValidationError, AccessDenied

class VeterinaryAdoption(models.Model):
    _name = "veterinary.adoption"
    _description = "Veterinary Adoption"

    name = fields.Char(string='Name',required=True,help='Name of the adoption')
    date_shelter_enter = fields.Date(string='Date Shelter enter')
    date_adoption = fields.Date(string='Date adoption')
    pet_id= fields.Many2one('veterinary.pet',string="Pet")
    contact_id= fields.Many2one('res.partner',string="Contact")
    state_id=fields.Many2one('veterinary.adoption.state',string="Adoption state",group_expand='_group_expand_stage')
    user_id=fields.Many2one('res.users',string="Responsible")
    day_shelter=fields.Integer(string="Days in shelter",compute="_compute_day_shelter")
    notes= fields.Text(string="Notes")
    adoption_fee=fields.Float(string="Adoption fee")
    color=fields.Integer(string="Color")
    image = fields.Image(string='Photo', related="pet_id.image")

    def _group_expand_stage(self, stages, domain, order):
        return stages.search([])
    
    
    @api.depends('date_shelter_enter')
    def _compute_day_shelter(self):
        for record in self:
                if record.date_shelter_enter:
                    record.day_shelter = (date.today() - record.date_shelter_enter).days
                else:
                    record.day_shelter = 0
    
    @api.constrains('date_adoption','date_shelter_enter')
    def _check_day(self):
      for record in self:
         if record.date_shelter_enter and record.date_adoption:
            if record.date_adoption<record.date_shelter_enter:
                raise ValidationError('Date adoption must be newer than date shelter')
