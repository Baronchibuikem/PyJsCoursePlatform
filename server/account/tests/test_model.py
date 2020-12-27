from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from ..models import CustomUser
from django.test.client import Client


class TestModels(TestCase):

    Student = {"username": 'Student',
               "email": "student@gmail.com", "user_type": "Student"}
    Instructor = {"username": "Instructor",
                  "email": "instructor@gmail.com", "user_type": "Instructor"}

    def setUp(self):
        """
        Setting up a defaul User
        """
        self.user_count = CustomUser.objects.count()
        self.new_student_user = CustomUser.objects.create(**self.Student)
        self.new_instructor_user = CustomUser.objects.create(**self.Instructor)
        self.new_student_user.set_password("student12345")
        self.new_student_user.save()
        self.new_instructor_user.set_password("instructor12345")
        self.new_instructor_user.save()

    def test_user_creation(self):
        """
        Here we test for user creation
        """
        self.assertEqual(CustomUser.objects.count() - self.user_count, 2)
        self.assertEqual(self.new_student_user.username, 'Student')
        self.assertTrue(self.new_student_user.password, 'student12345')
        self.assertEqual(self.new_instructor_user.username, 'Instructor')
        self.assertTrue(self.new_instructor_user.password, 'instructor12345')
