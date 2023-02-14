from django.test import SimpleTestCase
from bank_app.forms import Signup,Transfor,Login_form,Customer_Contactus

class TestForms(SimpleTestCase):

    def test_form_transfor_empty(self):
        form = Transfor(data={})
        self.assertFalse(form.is_valid())
    
    def test_form_login_empty(self):
        form = Login_form(data={})
        self.assertFalse(form.is_valid())

    def test_form_customer_contact_empty(self):
        form = Customer_Contactus(data={})
        self.assertFalse(form.is_valid())
    
    def test_signup_form(self):
        form = Signup({
            'first_name': 'a',
            'last_name' : 'b',
            'resident_addr' : 'pune',
            'office_addr' : 'pune',
            'phone_no' : '8362987612',
            'email' : 'a.b@gmail.com',
            'password' : 'test1234',
            'repassword' : 'test1234',
            'Balance' : 1000
        })

        self.assertTrue(form.is_valid())
        