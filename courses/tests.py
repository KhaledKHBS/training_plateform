from django.test import TestCase
from .models import Course, Instructor
from django.urls import reverse


class CourseTests(TestCase):
    def test_creation_course(self):
        prof = Instructor.objects.create(
            name="Leila", email="leila@example.test")
        cours = Course.objects.create(
            title="Django test", description="Test",
            price="20.00", duration=12, instructor=prof)
        self.assertEqual(cours.title, "Django test")

    def test_catalogue_repond(self):
        url = reverse("course_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


