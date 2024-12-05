from odoo import models, fields, api, _
from odoo.tools import date_utils
from odoo.exceptions import UserError, ValidationError

import logging
logger = logging.getLogger(__name__)


class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Veterinary Insurance'

    # Many2one
    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    insurance_company = fields.Char(string='Insurance Company')
    policy_number = fields.Char(string='Policy Number', copy=False)
    coverage_details = fields.Text(string='Coverage details')
    expiration_date = fields.Date(string='Expiration date', required=True,
                                  default=date_utils.add(fields.date.today(), months=1))
    expired = fields.Boolean(string='Expired', default=False)
    active = fields.Boolean(string="Active", default=True)

    # sql constraints
    _sql_constraints = [
        ('check_unique_policy_number', 'UNIQUE(policy_number)',
         'A Policy Number must be unique'),
    ]

    # methods
    def action_check_expiration_date(self):
        for record in self:
            logger.info('Checking %s: %s', record.id, record.expiration_date)
            if record.expiration_date:
                if record.expiration_date < fields.Date.today():
                    record.expired = True
                else:
                    record.expired = False
            # else:
            #     TODO: option raise messages
            #     raise UserError(_('Please indicate the expiration date!'))
            #     show success message
            #     title = _('Warning!')
            #     message = _('Please indicate the expiration date!')
            #     return {
            #         'type': 'ir.actions.client',
            #         'tag': 'display_notification',
            #         'params': {
            #             'title': title,
            #             'message': message,
            #             'sticky': False,
            #         }
            #     }

    def _cron_check_expiration_date(self):
        insurances = self.env['veterinary.insurance'].search([
            '|',
            ('active', '=', True),
            ('expired', '=', False)
        ])
        insurances.action_check_expiration_date()
        return True
