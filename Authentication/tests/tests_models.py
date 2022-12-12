from django.test import TestCase
from Authentication.models import *

# Create your tests here.
class Student(TestCase):
    def create_student (self):
        test_student = self.objects.create(
            student_id ='*************',
            password= ''
        )
        self.assertEqual(test_student.student_id)
        self.assertTrue(test_student.first_name)
        self.assertTrue(test_student.last_name)
        self.assertIsNotNone(test_student.email)
        self.assertIsNotNone(test_student.phone_number)
        self.assertIsNotNone(test_student.faculty)
        self.assertIsNotNone(test_student.program)
    