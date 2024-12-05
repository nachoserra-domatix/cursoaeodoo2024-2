from odoo import models, fields

class VeterinaryInsurance(models.Model):
   _name = "veterinary.insurance"
   _description = "Veterinary Insurance"
   _rec_name='policy_number'

   _inherit=['mail.thread','mail.activity.mixin']
   
   #name = fields.Char(string='Name',required=True,help='Name of the insurance')
   pet_id = fields.Many2one('veterinary.pet',string="Pet")
   insurance_company=fields.Char(string="Insurance company")
   policy_number=fields.Char(string="Policy number",copy=False)
   cover_details=fields.Text(string="Cover details")
   expiration_date=fields.Date(string="Expiration data",default=fields.Date.today)
   expired= fields.Boolean(string="Expired")
   active= fields.Boolean('Active',default=True)
   

   _sql_constraints=[
      ('policy_number_unique', 'unique(policy_number)','The policy number must be unique'),
   ]
   
   def _cron_check_expired(self):
      insurances=self.search([('active','=',True),('expired','=',False)])
      insurances.check_insurance_date()
      return True
   
   def check_insurance_date(self):
      for record in self:
         if record.expiration_date:
            if record.expiration_date < fields.Datetime.now().date():
                record.expired = True
                record.active = False
            else:
                record.expired=False