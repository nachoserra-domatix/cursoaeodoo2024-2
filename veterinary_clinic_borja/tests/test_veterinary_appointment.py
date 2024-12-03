from odoo.tests import common


class TestVeterinaryAppointment(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.test_partner = self.env["res.partner"].create(
            {"name": "partner_test", "email": "email_test", "phone": "666666666"}
        )
        self.test_partner_2 = self.env["res.partner"].create(
            {"name": "partner_test_2", "email": "email_test", "mobile": "666666666"}
        )
        self.test_pet = self.env["veterinary.pet"].create({"name": "pet_test"})
        self.test_appointment = self.env["veterinary.appointment"].create(
            {
                "partner_id": self.test_partner.id,
                "pet_id": self.test_pet.id,
                "reason": "reason_test",
                "duration_minutes": 5,
            }
        )
        self.test_done_tag = self.env["veterinary.appointment.tag"].create(
            {"name": "done", "code": "done"}
        )

    def test_onchange_assigned(self):
        self.test_appointment.assigned = False
        self.test_appointment._onchange_assigned()
        self.assertFalse(self.test_appointment.user_id)
        self.test_appointment.assigned = True
        self.test_appointment._onchange_assigned()
        self.assertEqual(self.test_appointment.user_id, self.env.user)

    def test_check_dates(self):
        with self.assertRaises(Exception):
            self.test_appointment.duration_minutes = -1

    def test_action_draft(self):
        self.test_appointment.action_draft()
        self.assertEqual(self.test_appointment.status, "draft")

    def test_onchange_partner_id(self):
        self.test_appointment._onchange_partner_id()
        self.assertEqual(self.test_appointment.partner_phone, self.test_partner.phone)
        self.test_appointment.partner_id = None
        self.test_appointment._onchange_partner_id()
        self.assertFalse(self.test_appointment.partner_phone)
        self.test_appointment.partner_id = self.test_partner_2.id
        self.test_appointment._onchange_partner_id()
        self.assertEqual(
            self.test_appointment.partner_phone, self.test_partner_2.mobile
        )

    def test_action_done(self):
        self.test_appointment.action_done()
        self.assertEqual(self.test_appointment.tag_ids[0].name, self.test_done_tag.name)
        self.assertEqual(self.test_appointment.tag_ids[0].code, self.test_done_tag.code)
        self.assertEqual(
            self.test_appointment.tag_ids[0].color, self.test_done_tag.color
        )
        self.assertEqual(self.test_appointment.status, "done")

    def test_create_tags(self):
        self.test_appointment.create_tags()
        self.assertEqual(
            self.test_appointment.tag_ids[0].name, self.test_appointment.reason
        )
        self.assertEqual(
            self.test_appointment.tag_ids[0].code, self.test_appointment.reason
        )
        test_tag_2 = self.env["veterinary.appointment.tag"].create(
            {"name": "reason_tag_2", "code": "reason_tag_2"}
        )
        self.test_appointment.reason = "reason_tag"
        self.test_appointment.create_tags()
        self.assertEqual(self.test_appointment.tag_ids[0].name, test_tag_2.name)
        self.assertEqual(self.test_appointment.tag_ids[0].code, test_tag_2.code)
        self.assertEqual(len(self.test_appointment.tag_ids), 2)
