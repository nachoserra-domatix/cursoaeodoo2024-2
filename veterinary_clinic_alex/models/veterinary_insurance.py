from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class VeterinaryInsurance(models.Model):
    _name= 'veterinary.insurance'
    _description = 'Veterinary Insurance'

    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    insurance_company = fields.Char(string='Insurance Company')
    insurance_number = fields.Char(string='Insurance Number')
    insurance_expiration_date = fields.Date(string='Insurance Expiration Date', default = fields.Date.today())
    coverage_details = fields.Text(string='Coverage Details', help='Details of the insurance coverage')
    expired = fields.Boolean(string='Expired')
    active = fields.Boolean(string='Active', default=True) #Este campo permite archivar registros es como un borrado logico

    _sql_constraints = [
        ('insurance_number_unique', 'UNIQUE(insurance_number)', 'The insurance number must be unique')
    ]

    def action_expired(self):
        for record in self:
            _logger.info('Checking insurance expiration date %s',record.id)
            _logger.info('Checking insurance expiration date {record.id}')
            if record.insurance_expiration_date:
                if (record.insurance_expiration_date >= fields.Date.today()):
                    record.expired = False
                else:
                    record.expired = True
    def _cron_check_expired(self):
        insurances = self.search([('active','=',True),('expired','=',False)])
        insurances.action_expired()
        return True