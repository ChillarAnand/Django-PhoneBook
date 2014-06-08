from django.test import TestCase

# Create your tests here.

from .models import person

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="krace", phone_no="23")
        Person.objects.create(first_name="adsfads", phone_no="11123")

    def test_startswith(self):
        self.assertEqual(person.objects.filter(filter_name__istartswith='f').count)
