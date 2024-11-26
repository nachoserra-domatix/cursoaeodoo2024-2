from odoo import fields, models
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class Insurance(models.Model):
    _name = "veterinary.insurance"
    _description = "Veterinary insurance"
    _rec_name = "policy_number"

    pet_id = fields.Many2one('veterinary.pet', string="Pet")
    insurance_company = fields.Char(string="Insurance company name")
    policy_number = fields.Integer(string="Policy Number", copy=False)
    coverage_details = fields.Text(string="Coverage Details")
    expiration_date = fields.Date(string="Expiration Date")
    status_expired = fields.Boolean(string="Status of insurance")
    active = fields.Boolean(string="Active", default=True)  # Campo reservado para archivar registros
    issuance_date = fields.Date(string='Issuance Date', default=fields.Date.today)

    _sql_constraints = [
        ("policy_number_unique", "unique (policy_number)", "The policy number must be unique")
    ]


    def action_expiration(self):
        current_date = fields.Date.today()
        for record in self:
            _logger.info(f"Cheking expiration date of insurance {record.id}")
            if record.expiration_date and record.expiration_date < current_date:
                record.status_expired = True
                # record.active = False
            else:
                record.status_expired = False

    def _cron_check_expired(self):
        insurances = self.search([])
        for insurance in insurances:
            insurance.action_expiration()
