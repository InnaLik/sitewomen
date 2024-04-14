from django.test import TestCase

# Create your tests here.
class TestUrl(TestCase):
    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)