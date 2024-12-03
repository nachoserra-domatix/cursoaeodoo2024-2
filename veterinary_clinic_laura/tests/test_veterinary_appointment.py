from odoo.tests import common

class TestVeterinaryAppointment(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.partner= self.env['res.partner'].create({'name':'Jose', 'email':'jose@gmail.com','phone':'666666666'})
        self.pet= self.env['veterinary.pet'].create({'name':'Rex'})
        self.appointment=self.env['veterinary.appointment'].create({
            'partner_id':self.partner.id,
            'pet_id':self.pet.id,
            'reason':'Reason 1'
        })


    def test_onchange_assigned(self):
        self.appointment.assigned=False
        self.appointment._onchange_assigned() #because onchange on view
        self.assertFalse(self.appointment.user_id)
        self.appointment.assigned=True
        self.appointment._onchange_assigned()
        self.assertEqual(self.appointment.user_id, self.env.user)
    
    def test_check_duration(self):
        with self.assertRaises(Exception):
            self.appointment.duration = -1
    
    def test_action_draft(self):
        self.appointment.action_draft()
        self.assertEqual(self.appointment.state,'draft')
    def test_onchange_partner_id(self):
        
        self.appointment._onchange_partner_id()
        self.assertEqual(self.appointment.partner_phone,self.appointment.partner_id.phone)
        self.appointment.partner_id=False
        self.appointment._onchange_partner_id()
        self.assertFalse(self.appointment.partner_phone)
    
    def test_action_done(self):
        self.appointment.action_done()
        self.assertEqual(self.appointment.state,'done')

    def test_create_tags(self):
        self.appointment.create_tags()
        tag_names = self.appointment.tag_ids.mapped('name')
        self.assertIn(self.appointment.reason, tag_names)

    
