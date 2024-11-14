from odoo import models, fields

class VeterinaryInsurance(models.Model):
    _name= 'veterinary.insurance'
    _description = 'Veterinary Insurance'

    pet_id = fields.Many2one('veterinary.pet', string='Pet', required=True)
    insurance_company = fields.Char(string='Insurance Company', required=True)
    insurance_number = fields.Char(string='Insurance Number', required=True)
    insurance_expiration_date = fields.Date(string='Insurance Expiration Date', required=True)
    coverage_details = fields.Text(string='Coverage Details', help='Details of the insurance coverage')
    expired = fields.Boolean(string='Expired')
    active = fields.Boolean(string='Active', default=True) #Este campo permite archivar registros es como un borrado logico

    def action_expired(self):
        for record in self:
            if record.insurance_expiration_date:
                if (record.insurance_expiration_date >= fields.Date.today()):
                    record.expired = True
                else:
                    record.expired = False
            