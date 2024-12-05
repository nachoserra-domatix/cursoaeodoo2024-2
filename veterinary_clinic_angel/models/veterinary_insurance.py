from odoo import models, fields

class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _description = 'Veterinary Insurance'
    _rec_name = 'policy_number'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    company = fields.Char(string='Company', required=True)
    policy_number = fields.Char(string='Policy Number', required=True, copy=False, default="New")
    coverage_details = fields.Text(string='Coverage Details')
    expiration_date = fields.Date(string='Expiration Date', required=True)
    expired = fields.Boolean(string='Expired', readonly=True)
    date = fields.Date(string='Date', default=fields.Date.today)
    _sql_constraints = [
        ('policy_number_unique', 'unique(policy_number)', 'The policy number must be unique')
    ]

    def check_if_expired(self):
        for record in self:
            if record.expiration_date:
                record.expired = record.expiration_date < fields.Date.today()

    def _cron_check_expired_date(self):
        insurances = self.search([('expired', '=', False)])
        insurances.check_if_expired()