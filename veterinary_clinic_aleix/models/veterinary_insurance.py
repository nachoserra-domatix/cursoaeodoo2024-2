from odoo import models, fields, api, _
from odoo.tools import date_utils
from odoo.exceptions import UserError, ValidationError


class VeterinaryInsurance(models.Model):
    _name = 'veterinary.insurance'
    _description = 'Veterinary Insurance'

    pet_id = fields.Many2one('veterinary.pet', string='Pet')
    insurance_company = fields.Char(string='Insurance Company')
    policy_number = fields.Char(string='Policy Number')
    coverage_details = fields.Text(string='Coverage details')
    expiration_date = fields.Date(string='Expiration date', required=True)
    expired = fields.Boolean(string='Expired', default=False)
    active = fields.Boolean(string="Active", default=True)

    # methods
    def action_check_expiration_date(self):
        for record in self:
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
