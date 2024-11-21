from odoo import models, fields

class VeterinaryAdoption(models.Model):
    _name= 'veterinary.adoption'
    _description = 'Veterinary Adoption'

    name = fields.Char(string='Name')
    entry_date = fields.Date(string='Entry Date')
    adoption_date = fields.Date(string='Adoption Date')
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    pet_id_image = fields.Image(string='Pet Image', related='pet_id.image', store=True, readonly=False)
    contact_id = fields.Many2one('res.partner', string='Contact')
    state_id = fields.Many2one('veterinary.adoption.state', string='State', group_expand='_group_expand_states')
    user_id = fields.Many2one('res.users', string='User')
    shelter_days = fields.Integer(string='Shelter Days', compute ="_compute_shelter_days")
    notes = fields.Text(string='Notes')
    adoption_price = fields.Float(string='Adoption Price')
    color = fields.Integer(string='Color')
    
    

    def _group_expand_states(self,states,domian,order):
        return self.state_id.search([])
    
    def _compute_shelter_days(self):
        for record in self:
            if record.adoption_date:
                record.shelter_days = (record.adoption_date - record.entry_date).days               

            else:
                if record.entry_date:
                    record.shelter_days = (fields.date.today() - record.entry_date).days
                else:
                    record.shelter_days = 0
                