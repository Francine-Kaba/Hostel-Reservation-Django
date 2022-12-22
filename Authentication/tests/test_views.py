import json
from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from django.contrib.auth import get_user_model
from Authentication.models import Faculty, Program, UserRole

class StudentTesting(APITestCase):
    def setUp(self):
        self.email = "maria6@example.com"
        self.password = "P@ssword1234!!@"  
        user_role_data = {
            "name" : "Admin"
        }
        self.role = UserRole.objects.create(**user_role_data)       
        self.faculty_name = 'Example Faculty Name'
        self.program_name = 'Example Program Name'

        self.faculty = Faculty.objects.create(name=self.faculty_name)
        self.program = Program.objects.create(name=self.program_name)


        self.user_data = {
            "first_name" : "Francine",
            "last_name" : "Maria",
            "role_id" : self.role.id,
            "email" : self.email,
            "position" : "Dean",
            "faculty": self.faculty,
            "program": self.program,
            "student_id": "*************",
            "password" : self.password
        }
        self.student = self.client.post(
            path=reverse('add_student'),
            data=self.user_data
        )

        login_data = {
            "email": self.email,
            "password": "P@ssword1234!!@"
        }
        token_response = self.client.post(
            path=reverse('Login'),
            data=login_data
        )
        self.token_pair = json.loads(token_response.content)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token_pair['data']['access']}"
        )

    def test_user_role(self):
        payload = {"name": "User Role Name"}
        response = self.client.post(
            path=reverse('add_user_roles'),
            data=payload,
        )
        message = json.loads(self.student.content)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'User role added succesfully!')

    def test_position(self):
        payload = {"name": "Position Name"}
        response = self.client.post(
            path=reverse('add_position'), 
            data=payload,  
        )
        message = json.loads(self.student.content)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Position added succesfully!')

    def test_faculty(self):
        payload = {"name": "Faculty Name"}
        response = self.client.post(
            path=reverse('add_faculty'), 
            data=payload,  
        )
        message = json.loads(self.student.content)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Faculty added succesfully!')

    def test_program(self):
        payload = {"name": "Program Name"}
        response = self.client.post(
            path=reverse('add_program'), 
            data=payload,  
        )
        message = json.loads(self.student.content)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Program added succesfully!')

    def test_add_admin(self):
        payload = {
            "first_name" : "FrancineExample",
            "last_name" : "Maria",
            "role_id" : self.role.id,
            "email" : "maria5@example.com",
            "position" : "Dean",
            "password" : self.password
        }
        response = self.client.post(
            path=reverse('add_admin'), 
            data=payload,  
        )
        message = json.loads(self.student.content)['message']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(message, 'Admin added succesfully')
    
    def test_student(self):
        message = json.loads(self.student.content)['message']
        self.assertEqual(self.student.status_code, 200)
        self.assertEqual(message, 'Student created sucessfully')
    




















