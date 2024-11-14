from odoo import fields, models
from datetime import datetime

class Insurance(models.Model):
    _name = "veterinary.insurance"
    _description = "Veterinary insurance"

    pet_id = fields.Many2one('veterinary.pet', string="Pet")
    insurance_company = fields.Char(string="Insurance company name")
    policy_number = fields.Integer(string="Policy Number")
    coverage_details = fields.Text(string="Coverage Details")
    expiration_date = fields.Date(string="Expiration Date")
    status_expired = fields.Boolean(string="Status of insurance")
    active = fields.Boolean(string="Active", default=True) #campo reservado para archivar registros
    
    def action_expiration(self):
        current_date = fields.Date.today()
        for record in self:
            if record.expiration_date and record.expiration_date < current_date:
                record.status_expired = True
                # record.active = False
            else:
                record.status_expired = False
