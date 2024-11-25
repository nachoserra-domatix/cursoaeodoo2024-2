from odoo import models, fields, api

class VeterinarySurgery(models.Model):
    _name = "veterinary.surgery"
    _description = "Veterinary Surgery"

    def _group_expand_states(self, states, domain,order):
      return [key for key ,val in type(self).state.selection]

    name = fields.Char(string='Name',required=True,help='Name of the surgery')
    pet_id = fields.Many2one('veterinary.pet',string="Pet")
    employee_id= fields.Many2one('hr.employee',string="Employee")
    surgery_date= fields.Date(string="Surgery date")
    state= fields.Selection([
        ('wait','Wait'),
        ('doing','Doing'),
        ('finish','Finish'),
    ],default='wait', string='State',group_expand="_group_expand_states")
    color=fields.Integer(string="color")
    line_ids=fields.One2many('veterinary.surgery.line','surgery_id',string="Lines")

    def _cron_check_surgery(self):
      surgeries_wait=self.search([('state','=','wait')])
      for surgery in surgeries_wait:
          if surgery.surgery_date < fields.Date.today():
              surgery.state='finish'

    def action_doing(self):
        for record in self:
            record.state='doing'

    def action_finish(self):
        for record in self:
            record.state="finish"
    
    def action_wait(self):
        for record in self:
            record.state="wait"