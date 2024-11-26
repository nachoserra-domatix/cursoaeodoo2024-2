from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _description = 'Veterinary Insurance'
    _rec_name = 'policy_number'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', help='Pet that has the insurance')
    insurance_company = fields.Char(string='Insurance Company', help='Insurance company')
    policy_number = fields.Char(string='Policy Number', help='Policy number', copy=False)
    coverage = fields.Text(string='Coverage', help='Coverage of the insurance')
    expiration_date = fields.Date(string='Expiration Date', help='Expiration date of the insurance', default=fields.Date.today)
    expired = fields.Boolean(string='Expired')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('policy_number_unique', 'unique (policy_number)', "Policy number must be unique"),]

    def check_expired(self):
        for record in self:
            _logger.info('Checking expiration date of insurance %s', record.id)
            #_logger.info(f'Checking expiration date ({record.expiration_date}) of insurance {record.id}')
            if record.expiration_date:
                if record.expiration_date < fields.Date.today():
                    record.expired = True
                    record.active = False
                else:
                    record.expired = False
    
    def _cron_check_expired(self):
        insurances = self.search(['|',('active', '=', True),(('expired', '=', False))])
        insurances.check_expired()
        return True