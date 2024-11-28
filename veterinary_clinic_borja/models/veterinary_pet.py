from odoo import fields, models, api


class VeterinaryPet(models.Model):
    _name = "veterinary.pet"
    _description = "Veterinary Pet"

    name = fields.Char(string="Name", required=True, help="Name of the pet")
    birthdate = fields.Date(string="Birthdate", help="Birthdate of the pet")
    weight = fields.Float(string="Weight", help="Weight of the pet")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    pet_number = fields.Char(
        string="Pet Number", help="Chip number of the pet", copy=False
    )
    species_id = fields.Many2one("veterinary.species", string="Species")
    vaccinated = fields.Boolean(
        string="Vaccinated",
        compute="_compute_vaccinated",
        inverse="_inverse_vaccinated",
        store=True,
    )
    last_vaccination_date = fields.Date(string="Last Vaccination Date")
    avatar = fields.Image("Avatar")
    allergy_ids = fields.Many2many("veterinary.allergy", string="Allergies")
    is_adopted = fields.Boolean(string="Adopted")
    appointment_ids = fields.One2many(
        "veterinary.appointment", "pet_id", string="appointments"
    )
    appointment_count = fields.Integer(compute="_compute_appointment_count")
    insurance_ids = fields.One2many(
        "veterinary.insurance", "pet_id", string="insurances"
    )
    insurance_count = fields.Integer(compute="_compute_insurance_count")
    surgery_ids = fields.One2many("veterinary.surgery", "pet_id", string="surgeries")
    surgery_count = fields.Integer(compute="_compute_surgery_count")
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        (
            "name_unique",
            "unique (pet_number, species_id)",
            "Chip number of the pet is unique by specie",
        ),
    ]

    def _compute_surgery_count(self):
        for record in self:
            record.surgery_count = len(record.surgery_ids)

    def _compute_insurance_count(self):
        for record in self:
            record.insurance_count = len(record.insurance_ids)

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)

    def action_view_surgeries(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Surgeries",
            "res_model": "veterinary.surgery",
            "view_mode": "tree,form",
            "domain": [("pet_id", "=", self.id)],
        }

    def action_view_insurances(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Insurances",
            "res_model": "veterinary.insurance",
            "view_mode": "tree,form",
            "domain": [("pet_id", "=", self.id)],
        }

    def action_view_appointments(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Appointments",
            "res_model": "veterinary.appointment",
            "view_mode": "tree,form",
            "domain": [("pet_id", "=", self.id)],
        }

    def action_vaccinated(self):
        self.vaccinated = True
        self.last_vaccination_date = fields.Date.today()

    @api.depends("birthdate")
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365

    def create_insurance(self):
        self.env["veterinary.insurance"].create(
            {
                "policy_number": "123123",
                "insurance_company": "allianz",
                "coverage_details": "details",
                "expiration_date": fields.Datetime.today(),
            }
        )

    @api.depends("last_vaccination_date")
    def _compute_vaccinated(self):
        for record in self:
            if record.last_vaccination_date:
                record.vaccinated = True

    def _inverse_vaccinated(self):
        for record in self:
            if record.vaccinated:
                record.last_vaccination_date = fields.Date.today()

    def surgeris_done(self):
        if self.ensure_one():
            surgeris = self.env["veterinary.surgery"].search([("pet_id", "=", self.id)])
            for surgery in surgeris:
                surgery.action_done()

    def action_print_appointments(self):
        appoinments = self.appointment_ids
        report = self.env.ref(
            "veterinary_clinic_borja.action_report_veterinary_appointment"
        ).report_action(appoinments.ids)
        return report
