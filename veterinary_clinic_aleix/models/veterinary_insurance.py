from odoo import models, fields


class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _description = 'Veterinary Insurance'

    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    insurance_company = fields.Char(string='Insurance Company')
    policy_number = fields.Char(string='Policy Number')
    coverage_details = fields.Text(string='Coverage details')
    expiration_date = fields.Date(string='Expiration date')
    expired = fields.Boolean(string='Expired', default=False)

    # methods
    def action_check_expiration_date(self):
        for record in self:
            if record.expiration_date < fields.Date.today():
                record.expired = True
            else:
                record.expired = False