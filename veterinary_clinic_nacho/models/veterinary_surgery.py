from odoo import fields, models


class VeterinarySurgery(models.Model):
    _name = 'veterinary.surgery'
    _description = 'Veterinary Surgery'

    name = fields.Char(string='Name', required=True, help='Name of the surgery')
    pet_id = fields.Many2one('veterinary.pet', string='Pet', help='Pet that will undergo the surgery')
    employee_id = fields.Many2one('hr.employee', string='Veterinarian', help='Veterinarian that will perform the surgery')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done')
    ], default='draft', string='State', help='State of the surgery')
    surgery_date = fields.Datetime(string='Surgery Date', help='Date of the surgery')


    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_done(self):
        for record in self:
            record.state = 'done'