from django.test import TestCase

from women.models import Women, Category


class TestUrl(TestCase):

    def setUp(self) -> None:
        Women.objects.create(title='lion', slug='lion', cat_id=1)
        Category.objects.create(name='Животные', slug='Animal')

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_get_absolute_url(self):
        women = Women.objects.get(title='lion')
        self.assertEqual(women.get_absolute_url(), '/post/lion/')
