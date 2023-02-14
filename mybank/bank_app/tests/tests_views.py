from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.landing_page = reverse('landingpage')
        self.home_page = reverse('homepage',args = ['DDB0000'])
        self.my_sign_up = reverse('mysignup')
        self.mylogin = reverse('mylogin')
        self.logout = reverse('logout')

    def test_landingpage_view(self):

        response = self.client.get(self.landing_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'landingpage.html')
    
    def test_my_sign_up_view(self):
        response = self.client.get(self.my_sign_up)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'mysignup.html')
    
    def test_login_view(self):
        response = self.client.get(self.mylogin)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'mylogin.html')
    
    def test_logout_view(self):
        response = self.client.get(self.logout)
        self.assertEqual(response.status_code, 302)
        