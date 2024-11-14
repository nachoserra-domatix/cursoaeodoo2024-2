from odoo import fields, models

class VeterinaryInsurance(models.Model):
    _name = "veterinary.insurance"
    _description = "Veterinary Insurance"

    pet_id = fields.Many2one("veterinary.pet", string="Pet")
    insurance_company = fields.Char(string="Insurance Company")
    policy_number = fields.Integer(string="Policy")
    coverage_details = fields.Text(string="Details", required=True)
    expiration_date = fields.Datetime(string="Date", required=True)
    expired = fields.Boolean(string="Expired")

    def action_check_expired(self):
        self.expired = self.expiration_date < fields.Datetime.today()