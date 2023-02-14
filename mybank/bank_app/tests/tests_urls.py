from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bank_app.views import landingpage,logoutpage,homepage,mylogin,mysignup

class TestUrls(SimpleTestCase): 

    def test_landingpage_url(self):
        url = reverse('landingpage')
        self.assertEqual(resolve(url).func, landingpage)
    
    def test_login_url(self):
        url = reverse('mylogin')
        self.assertEqual(resolve(url).func, mylogin)
    
    def test_homepage_url(self):
        url = reverse('homepage',args = ['DDB0000'])
        self.assertEqual(resolve(url).func, homepage)
    
    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logoutpage)
    
    def test_sign_up_url(self):
        url = reverse('mysignup')
        self.assertEqual(resolve(url).func, mysignup)