from django.shortcuts import render
from rest_framework.views import APIView
from Authentication.models import Student, Admin, UserRoles, Faculty, Program
from rest_framework.exceptions import AuthenticationFailed
from helpers.utils import validate_password
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse

# Create your views here.
"""
The AddUserRoles class creates and adds a new faculty into the database
"""
class AddUserRoles(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        UserRoles.objects.create(name=name)
        data = UserRoles.objects.filter().values('id', 'name')
        return JsonResponse({'message': 'User role added succesfully!', 'data': list(data)})

"""
The AddAdmin class creates and adds a new admin into the database
"""
class AddAdmin(APIView):
    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first name')
        last_name = request.data.get('last name')
        email = request.data.get('email')
        password = request.data.get('password')
        position = request.data.get('position')
        role_id = request.data.get('student id')

        try:
            Admin.objects.get(email=email)
            raise AuthenticationFailed("User already exists")
        except Admin.DoesNotExist:
            try:
                UserRoles.objects.get(id=role_id)

                details = {
                    'first_name' : first_name,
                    'last_name' : last_name,
                    'role_id' : role_id,
                    'email' : email,
                    'position': position,
                    'password' : make_password(password)
                }
                check_password = validate_password(password)   #password validation
                if check_password["status"]:
                    Admin.objects.create(**details)
                    data = Admin.objects.filter().values('id', 'first_name', 'last_name', 'role_id', 'email', 'position', 'password')
                    return JsonResponse({'message': 'Admin added succesfully', 'data': list(data)})
            except:
                return



"""
The AddFaculty class creates and adds a new faculty into the database
"""
class AddFaculty(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        Faculty.objects.create(name=name)
        data = Faculty.objects.filter().values('id', 'name')
        return JsonResponse({'message': 'Faculty added succesfully!', 'data': list(data)})

"""
The AddProgram class creates and adds a new program into the database
"""
class AddProgram(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        Program.objects.create(name=name)
        data = Program.objects.filter().values('id', 'name')
        return JsonResponse({'message': 'Program added succesfully!', 'data': list(data)})


"""
The AddStudent class creates and adds a new student into the database
"""
class AddStudent(APIView):
    def post(self, request, *args, **kwargs):
        student_id = request.data.get('student id')
        first_name = request.data.get('first name')
        last_name = request.data.get('last name')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone number')
        faculty = request.data.get('faculty')
        program = request.data.get('program')

        try: 
            Student.objects.get(student_id=student_id)
            raise AuthenticationFailed("User already exists")

        except Student.DoesNotExist:

            try:
                Student.objects.get(id=student_id)
                details = {
                    'student_id' : student_id,
                    'first_name' : first_name,
                    'last_name' : last_name,
                    'email' : email,
                    'password' : make_password(password),
                    'phone_number' : phone_number,
                    'faculty' : faculty,
                    'program' : program
                }  
                check_password = validate_password(password) # this code validates the password
                if check_password["status"]:
                    Student.objects.create(**details)  
                    data = Student.objects.filter().values(**details)
                    return JsonResponse({'message': 'Student added succesfully', 'data': list(data)})
            except:
                return

