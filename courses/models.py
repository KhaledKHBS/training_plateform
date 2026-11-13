from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL,
    null=True, blank=True, related_name="courses")


    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(
        Course, related_name="students", blank=True)

    def __str__(self):
        return self.name
class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="profile")
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

class CourseDocument(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE,
        related_name="documents"
    )
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="course_docs/")
