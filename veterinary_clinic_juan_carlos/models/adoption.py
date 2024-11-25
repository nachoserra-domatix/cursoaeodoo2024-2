from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Adoption(models.Model):
    _name = 'veterinary.adoption'
    _description = 'Pet Adoption'

    name = fields.Char(string='Name', required=True)
    entry_date = fields.Datetime(string='Date of Entry to Shelter')
    adoption_date = fields.Datetime(string='Adoption Date')
    pet_id = fields.Many2one('veterinary.pet', string='Pet', domain="[('adopted', '=', False)]")
    adopter_contact = fields.Many2one('res.partner', string='Adopter Contact')
    adoption_state = fields.Many2one('veterinary.adoption.state', string='Adoption State')
    responsible_user = fields.Many2one('res.users', string='Responsible User')
    days_in_shelter = fields.Integer(string='Days in Shelter', compute='_compute_days_in_shelter')
    notes = fields.Text(string='Notes')
    adoption_fee = fields.Float(string='Adoption Fee')
    pet_image = fields.Image(related='pet_id.pet_image', string="Pet Photo", readonly=True)
    adoption_state_bool = fields.Boolean(related='adoption_state.adopted', string="Adopted", readonly=False)

    def _compute_days_in_shelter(self):
        for record in self:
            if record.entry_date and record.adoption_date:
                adoption_date = fields.Datetime.from_string(record.adoption_date)
                entry_date = fields.Datetime.from_string(record.entry_date)
                delta = adoption_date - entry_date
                record.days_in_shelter = delta.days
            else:
                record.days_in_shelter = 0

    @api.constrains('adoption_date', 'entry_date')
    def _check_adoption_date(self):
        for record in self:
            if record.adoption_date and record.entry_date:
                if fields.Datetime.from_string(record.adoption_date) < fields.Datetime.from_string(record.entry_date):
                    raise ValidationError("Adoption date cannot be earlier than the entry date to the shelter.")
