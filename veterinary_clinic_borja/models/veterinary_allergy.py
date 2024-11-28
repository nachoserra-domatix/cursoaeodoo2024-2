from odoo import fields, models, api

class VeterinaryAllergy(models.Model):
   _name = "veterinary.allergy"
   _description = "Veterinary Allergy"

   name = fields.Char(string="Name", required=True, help="Name of the allergy")
   severity_degree = fields.Selection([
        ("very_high", "Very high"),
        ("high", "High"),
        ("normal", "Normal"),
        ("low", "Low")   
    ], default="normal", string="Severity degree")
   description = fields.Text(string="Description", required=True)
   is_severe = fields.Boolean(string="Is severe", compute="_compute_is_severe", store=True)

   @api.depends("severity_degree") 
   def _compute_is_severe(self):
        for record in self:
            if record.severity_degree == "very_high":
                record.is_severe = True
            else:
                record.is_severe = False