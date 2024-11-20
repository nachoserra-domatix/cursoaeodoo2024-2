from odoo import models, fields, api, Command

class Appointment(models.Model):
    _name = "veterinary.appointment"
    _description = "Veterinary Appointment"
    # _rec_name = "reason" #actua como nombre

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner")
    partner_phone = fields.Char(string="Partner Phone", related='partner_id.phone', store=True, readonly=False)
    partner_email = fields.Char(string="Partner email", related='partner_id.email', store=True, readonly=False)
    appointment_date = fields.Datetime(string="Appointment Date", help="Date and time", default=fields.Datetime.now)
    solution = fields.Html(string='Solution', help='Solution to the problem')
    reason = fields.Text(string="Reason for Appointment", help="reason")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default="draft", help="current status of the appointment")
    duration = fields.Float(string="Duration (minutes)", help="Duration minutes")
    user_id = fields.Many2one("res.users", string="Responsible")
    sequence = fields.Integer(string="Sequence", default=10)
    urgency = fields.Boolean(string="Urgent")
    color = fields.Integer(string="Color")
    assigned = fields.Boolean(string="Assigned", compute="_compute_assigned", inverse="_inverse_assigned", store=True)
    # test = fields.Boolean(string="test", compute="_compute_assigned")
    tag_ids = fields.Many2many("veterinary.appointment.tag", string="Tag")
    line_ids = fields.One2many("veterinary.appointment.line","appointment_id", string="line ids")

    def _inverse_assigned(self):
        for record in self:
            # import pdb;pdb.set_trace()
            if record.assigned:
                record.user_id = self.env.user
            else:
                record.user_id = False

    @api.depends("user_id")
    # @api.depends("user_id.phone")
    # @api.depends("user_id", "state", "appointment_date")
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)
            # record.test = ....

    def action_draft(self):
        for record in self:
            record.state = "draft"
            # import pdb;pdb.set_trace()

    def action_done(self):
        for record in self:
            record.state = "done"

    def action_cancelled(self):
        for record in self:
            record.state = "cancelled"

    def create_tags(self):
        tag_ids = self.env["veterinary.appointment.tag"].search([('name', 'ilike', self.reason)])
        # para añadir etiquetas existentes
        # tag_ids |= self.tag_ids
        if tag_ids:
            self.tag_ids = [Command.set(tag_ids.ids)]
        else:
            self.tag_ids = [Command.create({"name": self.reason})]

    # def button_add_tag(self):
    #     for record in self:
    #         record.tag_ids = [(0,0,{"name":"etiqueta3"})]
            # record.tag_ids = [Command.create({"name":"etiqueta3"})]
            # record.tag_ids = [Command.delete({"name":"etiqueta3"})]
            # pets = self.env['veterinary.pet'].search([('age', '>', 2), ('weight', '>', 2)], limit="1")
            # pets = self.env['veterinary.pet'].browse([1,3,4])


    # def action_draft(self):
    #     self.state = "draft"

    # def action_all_draft(self):
    #     appointments = self.search([])
    #     appointments.action_draft()