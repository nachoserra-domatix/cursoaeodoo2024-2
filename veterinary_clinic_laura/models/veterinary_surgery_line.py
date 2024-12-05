from odoo import models, fields,api, Command

class VeterinarySurgeryLine(models.Model):
   _name = "veterinary.surgery.line"
   _description = "Veterinary Surgery Line"
   
   name=fields.Char(string="Name",required=True)
   sequence=fields.Integer(string="Sequence")
   state= fields.Selection([
        ('wait','Wait'),
        ('doing','Doing'),
        ('finish','Finish'),
    ],default='wait', string='State')
   surgery_id=fields.Many2one('veterinary.surgery',string="Surgery")