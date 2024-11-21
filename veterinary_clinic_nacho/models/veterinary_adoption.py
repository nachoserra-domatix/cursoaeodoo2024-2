from odoo import fields,models,api

class VeterinaryAdoption(models.Model):
    _name = 'veterinary.adoption'
    _description = 'Veterinary Adoption'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    adoption_date = fields.Date(string='Adoption Date')
    pet_id = fields.Many2one('veterinary.pet', string='Pet',)
    partner_id = fields.Many2one('res.partner', string='Partner')
    stage_id = fields.Many2one('veterinary.adoption.stage', string='Stage', group_expand='_group_expand_stage')
    user_id = fields.Many2one('res.users', string='User')
    days_in_refugee = fields.Integer(string='Days in Refugee', compute='_compute_days_in_refugee')
    notes = fields.Text(string='Notes')
    price = fields.Monetary(string='Price')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    photo = fields.Image(string='Photo', related="pet_id.photo")

    def _group_expand_stage(self, stages, domain, order):
        return stages.search([])

    def _compute_days_in_refugee(self):
        for record in self:
            if record.start_date and record.adoption_date:
                adoption_date = fields.Datetime.from_string(record.adoption_date)
                entry_date = fields.Datetime.from_string(record.start_date)
                delta = adoption_date - entry_date
                record.days_in_refugee = delta.days
            else:
                record.days_in_refugee = 0

