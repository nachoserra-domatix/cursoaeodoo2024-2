from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, AccessDenied
import random
import string

class VeterinaryPet(models.Model):
   _name = "veterinary.pet"
   _description = "Veterinary Pet"

   name = fields.Char(string='Name',required=True,help='Name of the pet')
   birthdate = fields.Date(string='Birth Date')
   weight=fields.Float(string='Weight',help='Birth of the pet')
   age = fields.Integer(string="Age",compute="_compute_age",store=True)
   pet_number= fields.Char(string='Pet Number', help='Number of the pet')
   species_id= fields.Many2one('veterinary.species',string="Species")
   sequence = fields.Integer(string="Sequence",default=10)
   user_id = fields.Many2one('res.users',string="Responsible")
   vaccinated = fields.Boolean(string="Vaccinated",compute="_compute_vaccinated",inverse="_inverse_vaccinated")
   last_vaccination_date=fields.Date(string="Last vaccination date")
   image=fields.Image(string="Image")
   adopted=fields.Boolean(string="Adopted")
   allergy_ids=fields.Many2many('veterinary.allergy',string="Allergies")
   appointment_ids=fields.One2many('veterinary.appointment','pet_id',string="Appointments")
   appointment_count=fields.Integer(string="Appointment Count",compute="_compute_appointment_count")
   insurance_count=fields.Integer(string="Insurance Count",compute="_compute_insurance_count")
   insurance_ids=fields.One2many('veterinary.insurance','pet_id',string="Insurances")
   active=fields.Boolean(string="Active",default=True)
   surgery_count=fields.Integer(string="Insurance Count",compute="_compute_surgery_count")

   _sql_constraints=[
      ('number_species_unique', 'unique(pet_number,species_id)',"Can't repeat pet number and specie ")
   ]

   
   def action_print_appointments(self):
      appointments=self.appointment_ids
      report = self.env.ref('veterinary_clinic_laura.action_report_veterinary_appointment').report_action(appointments.ids)
      return report
   
   def _compute_appointment_count(self):
      for record in self:
         record.appointment_count= len(record.appointment_ids)
   
   def _compute_insurance_count(self):
      for record in self:
         insurances=self.env['veterinary.insurance'].search([('pet_id','=',self.id)])
         record.insurance_count=len(insurances)
   
   def _compute_surgery_count(self):
      for record in self:
         surgeries=self.env['veterinary.surgery'].search([('pet_id','=',record.id)])
         record.surgery_count=len(surgeries)
      

   def action_view_medical_history(self):
      return{
         'type':'ir.actions.act_window',
         'name':'Medical History',
         'res_model':'veterinary.appointment',
         'view_mode':'tree,form,kanban',
         'domain':[('pet_id','=',self.id)]

      }
   
   def action_view_insurance_history(self):
      return{
         'type':'ir.actions.act_window',
         'name':'Insurance History',
         'res_model':'veterinary.insurance',
         'view_mode':'tree,form,kanban',
         'domain':[('pet_id','=',self.id)]

      }
  
   def action_view_surgery_history(self):
      return{
         'type':'ir.actions.act_window',
         'name':'Surgery History',
         'res_model':'veterinary.surgery',
         'view_mode':'tree,form,kanban',
         'domain':[('pet_id','=',self.id)]

      }
   
   def _compute_vaccinated(self):
      for record in self:
         if record.last_vaccination_date:
            record.vaccinated=True
         else:
            record.vaccinated=False
   
   def _inverse_vaccinated(self):
      for record in self:
         if record.vaccinated:
            record.last_vaccination_date=fields.Datetime.now().date()
   
   @api.depends('birthdate')
   def _compute_age(self):
      for record in self:
         if record.birthdate:
            record.age=(fields.Date.today() - record.birthdate).days //365
         else:
            record.age = 0

   def action_vaccinated(self):
      for record in self:
         record.vaccinated=True
         record.last_vaccination_date=fields.Datetime.now()

   def action_set_pet_number(self):
      def generate_string():
         numbers = ''.join(random.choices(string.digits, k=8))  
         char = random.choice(string.ascii_uppercase)          
         result = numbers + char                            
         return result
      
      for record in self:
         record.pet_number=generate_string()

   def create_insurance(self):
      #import pdb; pdb.set_trace()
      self.copy({'name':'Copy of '+self.name})
      #self.env['veterinary.insurance'].create({'name':'name',
      #                                         'policy_number':'1234',
      #                                         'insurance_company':'AXA'})
   
   def surgery_complete_pet(self):
      surgery_ids= self.env['veterinary.surgery'].search([('pet_id','=',self.id)])
      surgery_ids.action_finish()