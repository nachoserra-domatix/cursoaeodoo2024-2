from odoo import fields, models, api
import random
import string

class VeterinaryPet(models.Model):
    _name = 'veterinary.pet'
    _description = 'Veterinary Pet'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    weight = fields.Float(string='Weight')
    age = fields.Integer(string='Age', compute="_compute_age", store=True)
    pet_number = fields.Char(string='Pet Number', help='Number of the pet')
    species_id = fields.Many2one('veterinary.species', string='Species', required=True)
    notes = fields.Text(string='Notes')
    vaccinated = fields.Boolean(string='Vaccinated', default=False, compute="_compute_vaccinated", store=True, inverse="_inverse_vaccinated")
    last_vaccination_date = fields.Date(string='Last Vaccination Date')
    surgery_ids = fields.One2many('veterinary.surgery', 'pet_id', string='Surgeries')
    image = fields.Image(string='Pet Photo')
    allergy_ids = fields.Many2many('veterinary.allergy', string='Allergies')
    adopted = fields.Boolean(string='Adopted', default=False)

    @api.depends('last_vaccination_date')
    def _compute_vaccinated(self):
        for record in self:
            record.vaccinated = bool(record.last_vaccination_date)
    
    def _inverse_vaccinated(self):
        for record in self:
            if not record.vaccinated:
                record.last_vaccination_date = False
            elif record.vaccinated and record.last_vaccination_date is False:
                record.last_vaccination_date = fields.Date.today()

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365

    def action_vaccinated(self):
        self.vaccinated = True
        self.last_vaccination_date = fields.Date.today()

    def action_get_pet_number(self):
        while True:
            pet_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=6))
            if not self.env['veterinary.pet'].search([('pet_number', '=', pet_number)]):
                self.pet_number = pet_number
                break

    def action_create_insurance(self):
        self.env['veterinary.insurance'].create({
            'pet_id': self.id,
            'policy_number': '1234',
        })

    def action_finish_surgeries(self):
        for surgery in self.surgery_ids:
            surgery.write({'state': 'done'})
            