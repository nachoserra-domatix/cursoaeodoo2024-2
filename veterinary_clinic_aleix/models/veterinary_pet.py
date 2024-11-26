from odoo import models, fields, api
import random


class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True, help='Name of the pet')
    birthday = fields.Date(string='Birthday', help='Birthday of the pet')
    weight = fields.Float(string='Weight', help='Weight of the pet')
    pet_number = fields.Char(
        string='Pet Number', help='Number of the pet', copy=False)
    # species = fields.Selection(
    #    [('cat', 'Cat'), ('dog', 'Dog'), ('bird', 'Bird'), ('other', 'Other')],
    #    string='Species'
    #  )
    last_vaccination_date = fields.Date(string="Last Vaccination Date")
    image = fields.Image(string='Pet image', max_width=1024, max_height=1024)
    adopted = fields.Boolean(string='Adopted', default=False)
    # One2many
    appointment_ids = fields.One2many(
        comodel_name='veterinary.appointment', inverse_name='pet_id')
    insurance_ids = fields.One2many(
        comodel_name='veterinary.insurance', inverse_name='pet_id')
    # Many2one
    species_id = fields.Many2one('veterinary.species', string='Species')
    # Many2many
    allergy_ids = fields.Many2many(
        comodel_name='veterinary.allergy', string='Allergies')
    # computed fields
    age = fields.Integer(string='Age', help='Age of the pet',
                         compute='_compute_age', store=True)
    vaccinated = fields.Boolean(
        string="Vaccinated", default=False, compute='_compute_vaccinated', inverse='_inverse_vaccinated', store=True)
    appointment_count = fields.Integer(
        string='Appointment Count', compute='_compute_appointment_count')
    insurance_count = fields.Integer(
        string='Insurance Count', compute='_compute_insurance_count')

    # sql constraints
    _sql_constraints = [
        ('check_unique_name', 'UNIQUE(name)',
         'A name must be unique'),
    ]

    # computed methods
    # @api.depends és necesario para un campo compute con store=True
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = (fields.Date.today() -
                              record.birthday).days // 365

    @api.depends('last_vaccination_date')
    def _compute_vaccinated(self):
        for record in self:
            if record.last_vaccination_date:
                record.vaccinated = True
            else:
                record.vaccinated = False

    def _inverse_vaccinated(self):
        for record in self:
            if record.vaccinated:
                record.last_vaccination_date = fields.Date.today()
            else:
                record.last_vaccination_date = None

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = len(record.insurance_ids)

    # action methods
    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()

    def action_random_pet_number(self):
        for record in self:
            record.pet_number = 'PET-' + str(random.randint(1, 999999))

    def action_view_appointment_history(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment History',
            'res_model': 'veterinary.appointment',
            'view_mode': 'tree,form,kanban',
            'domain': [('pet_id', '=', self.id)],
        }

    def action_view_insurances_pet(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Insurances Pet',
            'res_model': 'veterinary.insurance',
            'view_mode': 'tree,form,kanban',
            'domain': [('pet_id', '=', self.id)],
        }

    # methods
    def create_insurance(self):
        self.env['veterinary.insurance'].create(
            {'insurance_company': 'Company Test', 'policy_number': '1234'})
        # self.copy({'name': 'copy of' + self.name})

    # orm methods
    def set_all_surgery_as_done(self):
        surgeries = self.env['veterinary.surgery'].search(
            [('pet_id', '=', self.id)])
        surgeries.action_done()
