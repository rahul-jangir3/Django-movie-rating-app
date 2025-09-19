from django.test import TestCase
from .models import Movie

class MovieModelTest(TestCase):
    def test_create_movie(self):
        m = Movie.objects.create(title='Test Film', rating=7.5)
        self.assertEqual(m.title, 'Test Film')
        self.assertEqual(float(m.rating), 7.5)

