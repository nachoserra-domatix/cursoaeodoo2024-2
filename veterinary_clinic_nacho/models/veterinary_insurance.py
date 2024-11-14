from odoo import fields, models


class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _description = 'Veterinary Insurance'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', help='Pet that has the insurance')
    insurance_company = fields.Char(string='Insurance Company', help='Insurance company')
    policy_number = fields.Char(string='Policy Number', help='Policy number')
    coverage = fields.Text(string='Coverage', help='Coverage of the insurance')
    expiration_date = fields.Date(string='Expiration Date', help='Expiration date of the insurance')
    expired = fields.Boolean(string='Expired')
    active = fields.Boolean(string='Active', default=True)

    def check_expired(self):
        for record in self:
            if record.expiration_date:
                if record.expiration_date < fields.Date.today():
                    record.expired = True
                    record.active = False
                else:
                    record.expired = False