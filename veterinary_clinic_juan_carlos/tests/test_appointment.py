from odoo.tests.common import TransactionCase

class TestVeterinaryAppointment(TransactionCase):

    def setUp(self):
        super(TestVeterinaryAppointment, self).setUp()

        self.partner = self.env["res.partner"].create({
            "name": "Jesusito",
            "email": "jesus@pepito.com"
        })

        self.pet = self.env["veterinary.pet"].create({
            "name": "MascotaTest"
        })

        self.appointment = self.env["veterinary.appointment"].create({
            "partner_id": self.partner.id,
            "pet_id": self.pet.id,
        })

        self.existing_tag = self.env['veterinary.appointment.tag'].create({'name': 'test_tag'})

    def test_onchange_assigned_user(self):

        self.appointment.assigned = False
        self.appointment._onchange_assigned_user()
        self.assertFalse(self.appointment.user_id)

        self.appointment.assigned = True
        self.appointment._onchange_assigned_user()
        self.assertEqual(self.appointment.user_id, self.env.user)

    def test_onchange_partner_id_phone(self):
        self.assertFalse(self.appointment.partner_phone)

        self.partner.phone = "123456789"
        self.appointment.partner_id = self.partner
        self.appointment._onchange_partner_id_phone()
        self.assertEqual(self.appointment.partner_phone, "123456789")

        self.appointment.partner_id = False
        self.appointment._onchange_partner_id_phone()
        self.assertFalse(self.appointment.partner_phone)

    def test_check_duration(self):
        with self.assertRaises(Exception):
            self.appointment.duration = -1

    def test_action_draft(self):
        self.appointment.action_draft()
        self.assertEqual(self.appointment.state, "draft")

    def test_action_done(self):
        self.appointment.action_done()
        self.assertEqual(self.appointment.state, "done")

    def test_create_tags(self):
        self.appointment.reason = 'test_tag'
        self.appointment.create_tags()
        self.assertIn(self.existing_tag.id, self.appointment.tag_ids.ids)