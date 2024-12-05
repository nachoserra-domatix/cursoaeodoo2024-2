from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit='sale.order'

    appointment_id=fields.Many2one('veterinary.appointment',string="Appointment")
    insurance_ids=fields.One2many('veterinary.insurance','order_id',string="Insurances")
    insurance_count=fields.Integer(string="Insurance Count",compute="_compute_insurance_count")

    def _compute_insurance_count(self):
      for record in self:
         record.insurance_count= len(record.insurance_ids)
    
    
    def action_view_order_insurances(self):
      return{
         'type':'ir.actions.act_window',
         'name':'Order insurances',
         'res_model':'veterinary.insurance',
         'view_mode':'tree,form',
         'domain':[('order_id','=',self.id)]

      }
    
    
    def action_confirm(self):
        res= super().action_confirm()
        for line in self.order_line:
            if line.product_id.is_insurance:
                insurance=self.env['veterinary.insurance'].create({
                    'insurance_company':'Insurance from product '+line.product_id.name,
                    'order_id':self.id,
                })
                insurance.message_post(
                body=f"Insurance policy created from sale order {self.name}.",
                subject="New Insurance Created",
                )
                
        return res