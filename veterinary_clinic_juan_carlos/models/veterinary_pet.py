from odoo import models, fields
import random
import string

def generate_random_chip(lengk=12):
    caract = string.ascii_letters + string.digits
    return ''.join(random.choices(caract, k=lengk))


class VeterinaryPet(models.Model):
    _name = "veterinary.pet"
    _description = "Veterinary Pet"

    name = fields.Char(string="Name", required=True, help="Name of the pet", default="garritas")
    birthdate = fields.Date(string="Birthdate", help="Birthdate of the pet")
    weight = fields.Float(string="Weight")
    age = fields.Integer(string="Age")
    number_pet = fields.Char(string="Number Pet")
    # species = fields.Selection([
    #     ("cat", "Cat"),
    #     ("dog", "Dog"),
    #     ("other", "Other"),
    #     ("bird", "Bird"),
    # ])
    vaccinated = fields.Boolean(string="Vaccinated")
    last_vaccination_date = fields.Date(string="Last Vaccination Date")
    
    def action_vaccinated(self):
        for record in self:
            record.vaccinated = True
            record.last_vaccination_date = fields.Date.today()


    def action_chip_number_pet(self):
        for record in self:
            record.number_pet = generate_random_chip()
