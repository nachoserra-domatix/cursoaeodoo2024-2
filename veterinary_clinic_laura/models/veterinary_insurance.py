from odoo import models, fields

class VeterinaryInsurance(models.Model):
   _name = "veterinary.insurance"
   _description = "Veterinary Insurance"

   name = fields.Char(string='Name',required=True,help='Name of the insurance')
   pet_id = fields.Many2one('veterinary.pet',string="Pet")
   insurance_company=fields.Char(string="Insurance company")
   policy_number=fields.Char(string="Policy number")
   cover_details=fields.Text(string="Cover details")
   expiration_date=fields.Date(string="Expiration data")
   expired= fields.Boolean(string="Expired")
   active= fields.Boolean('Active',default=True)
   
   def check_insurance_date(self):
      for record in self:
         if record.expiration_date:
            if record.expiration_date < fields.Datetime.now().date():
                record.expired = True
                record.active = False
            else:
                record.expired=False