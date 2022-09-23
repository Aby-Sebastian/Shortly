from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_login(self):
        response = self.client.get('/account/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/account/logout/')
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.get('/account/register/')
        self.assertEqual(response.status_code, 200)