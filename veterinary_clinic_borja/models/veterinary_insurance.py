from odoo import fields, models
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)

class VeterinaryInsurance(models.Model):
    _name = "veterinary.insurance"
    _description = "Veterinary Insurance"

    pet_id = fields.Many2one("veterinary.pet", string="Pet")
    insurance_company = fields.Char(string="Insurance Company")
    policy_number = fields.Integer(string="Policy")
    coverage_details = fields.Text(string="Details", required=True)
    expiration_date = fields.Datetime(string="Date", required=True, default=fields.Datetime.today()+relativedelta(day=7))
    expired = fields.Boolean(string="Expired")
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('policy_number_unique', 'unique (policy_number)', "The policy number name must be unique"),]

    def action_check_expired(self):
        for record in self:
            _logger.info("Check insurance id : %s", record.id)
            is_expired = record.expiration_date < fields.Datetime.today()
            if(is_expired):
                record.expired = True
                record.active = False
            else:
                record.expired = False
    
    def _cron_check_expired(self):
        insurances = self.search(["|",("active", "=", True), ("expired","=",False)])
        insurances.action_check_expired()
        return True