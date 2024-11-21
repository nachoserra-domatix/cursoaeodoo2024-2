from odoo import models, fields, api

class VeterinaryAdoption(models.Model):
    _name = 'veterinary.adoption'
    _description = 'Veterinary Adoption'

    name = fields.Char(string='Name', required=True)
    entry_date = fields.Date(string='Entry Date')
    adoption_date = fields.Date(string='Adoption Date')
    pet_id = fields.Many2one('veterinary.pet', string='Pet', domain="[('adopted','=',False)]")
    pet_id_image = fields.Image(string="Pet Photo", related="pet_id.image", store=True)
    partner_id = fields.Many2one('res.partner', string="Partner")
    state_id = fields.Many2one('veterinary.adoption.state', string='Adoption State', group_expand='_group_expand_states')
    user_id = fields.Many2one('res.users', string='Responsible User')
    days_in_shelter = fields.Integer(string='Days in Shelter', compute='_compute_days_in_shelter')
    notes = fields.Text(string='Notes')
    price = fields.Monetary(string='Price')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    color = fields.Integer(string='Color')

    @api.model
    def _group_expand_states(self, states, domain, order):
        return states.search([])

    @api.depends('entry_date', 'adoption_date')
    def _compute_days_in_shelter(self):
        for record in self:
            if record.entry_date and record.adoption_date:
                delta = record.adoption_date - record.entry_date
                record.days_in_shelter = delta.days
            else:
                record.days_in_shelter = 0