from odoo import fields, models

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