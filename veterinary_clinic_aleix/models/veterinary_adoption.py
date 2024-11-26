from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class VeterinaryAdoption(models.Model):
    _name = 'veterinary.adoption'
    _description = 'Veterinary Adoption'

    name = fields.Char(string='Name', required=True)
    date_shelter_entry = fields.Date(string='Shelter entry date')
    date_adoption = fields.Date(string='Adoption date')
    notes = fields.Html(string='Notes')
    price = fields.Float(string='Price')
    color = fields.Integer(string='Color')
    # Many2one
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    partner_id = fields.Many2one('res.partner', string='Partner')
    stage_id = fields.Many2one(
        'veterinary.adoption.stage', string='Adoption stage', group_expand='_group_expand_stage')
    user_id = fields.Many2one('res.users', string='Responsible')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    # related fields
    pet_image = fields.Image(
        related='pet_id.image', string='Pet image')
    adopted = fields.Boolean(string='Adopted', related='stage_id.adopted')
    # computed
    days_in_shelter = fields.Integer(
        string='Days in shelter', compute='_compute_days_in_shelter')

    # computed methods
    def _compute_days_in_shelter(self):
        for record in self:
            if record.date_shelter_entry and record.date_adoption:
                record.days_in_shelter = (
                    record.date_adoption - record.date_shelter_entry).days
            else:
                record.days_in_shelter = 0

    # api constrains
    @api.constrains('date_adoption')
    def check_date_adoption(self):
        for record in self:
            if record.date_adoption:
                if record.date_adoption < record.date_shelter_entry:
                    raise ValidationError(
                    _('The Adoption date must be greater than Shelter entry date')
                )

    # método odoo para forzar que salgan todos los estados en la vista kanban
    def _group_expand_stage(self, stages, domain, order):
        return stages.search([])
