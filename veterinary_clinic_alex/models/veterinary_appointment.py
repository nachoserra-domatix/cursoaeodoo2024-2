from odoo import models, fields

class VeterinaryAppointment(models.Model):
    _name = 'veterinary.appointment'
    _description = 'Veterinary Appointment'
    #_rec_name = 'reason' # Permite establecer el campo que va actuar como name cuando el campo name no exista 

    name = fields.Char(string='Name', required=True,)
    date = fields.Datetime(string='Date', required=True, default =fields.Datetime.now, help='Date of the appointment')
    reason = fields.Text(string='Reason', help='Description of the appointment')
    solution = fields.Html(string='Solution', help='Solution of the appointment')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft', string='State', help='State of the appointment')

    duration = fields.Float(string='Duration', help='Duration of the appointment')
    user_id = fields.Many2one('res.users', string='Responsible', help='Veterinarian in charge of the appointment')
    sequence = fields.Integer(string='Sequence', default = 10)
    urgency = fields.Boolean(string='Urgent', help='Urgent appointment')

    def action_draft(self):
        for record in self:
            record.state = 'draft'   

    def action_done(self):
        for record in self:
            record.state = 'done'
        
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'