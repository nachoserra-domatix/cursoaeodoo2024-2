from odoo import fields, models

class VeterinaryVeterinarian(models.Model):
    _name = "veterinary.veterinarian"
    _description = "veterinary_veterinarian"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one("res.partner", string="Partner", required=True, ondelete="restrict")
    license_number = fields.Char(string="License Number")