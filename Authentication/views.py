from django.shortcuts import render
from rest_framework.views import APIView
from Authentication.models import Student, UserRole, Faculty, Program, User, Position, Student
from rest_framework.exceptions import AuthenticationFailed
from helpers.status_codes import (InvalidPassword, InvalidUser, UserAlreadyExist, WrongCredentials,
StudentAlreadyExists  )
from helpers.utils import validate_user_input, validate_login_user_input
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
"""
The AddUserRoles class creates and adds a new faculty into the database
"""
class AddUserRoles(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        # this if statement makes sure only a super admin can add new user roles
        if self.request.user.role_id == 1:    
            # this try catches any errors that may occur when saving a new user role into the database
            try:                              
                name = request.data.get('name')
                UserRole.objects.create(name=name)
                data = UserRole.objects.filter().values('id', 'name')
                return JsonResponse({'message': 'User role added successfully!', 'data': list(data)})
            except Exception:
                return JsonResponse({'message': 'Cannot add user role'})
        else:
            raise InvalidUser ('Invalid user, Not authorized')

"""
The AddPosition class creates and adds a new position into the database
"""
class AddPosition(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
         # this if statement makes sure only a super admin can add new user roles
        if self.request.user.role_id == 1:    
            # this try catches any errors that may occur when saving a new user role into the database        
            try:                              
                name = request.data.get('name') 
                Position.objects.create(name=name)
                data = Position.objects.filter(name=name).values('id', 'name')
                return JsonResponse({'message': 'Position added successfully!', 'data': list(data)})
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'Cannot add user role'})
        else:
            raise InvalidUser ('Invalid user, Not authorized')


"""
The AddAdmin class creates and adds a new admin into the database
"""
class AddAdmin(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
         # this if statement makes sure only a super admin can add new user roles
        if self.request.user.role_id == 1:         
             # the codes here takes the data from the frontend
            first_name = request.data.get('first_name')           
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            password = request.data.get('password')
            phone_number = request.data.get('phone_number')
            position = request.data.get('position')
            role_id = request.data.get('role_id')
            # this try and catch ensures that a user is not added twice
            try:                                                
                User.objects.get(email=email)
                return JsonResponse({"message": "User already exists"})
            except User.DoesNotExist:
                # this try and catch ensures that the role and position are already in the database
                try:                                        
                    role = UserRole.objects.get(id=role_id)
                    position = Position.objects.create(name=position)
                    details = {
                        'first_name' : first_name,
                        'last_name' : last_name,
                        'email' : email,
                        'phone_number': phone_number,
                        'position': position,
                        'role': role,
                        'password' : make_password(password)
                    }
                    # this validates user input
                    validation_response = validate_user_input(email, first_name, last_name, password)       
                    if validation_response is not None:
                        return validation_response
                    else:
                         # this creates an admin based on the details from above
                        User.objects.create(**details)             
                        data = User.objects.filter(email=email).values('id', 'email')
                        return JsonResponse({'message': 'Admin added successfully', 'data': list(data)})
                except Exception as e:
                    print("error", e)
                    return JsonResponse({'message': 'Cannot add admin, Not authorized'})
        else:
            return JsonResponse({'message': 'Cannot add admin, Not authorized'})

"""
The AddFaculty class creates and adds a new faculty into the database
"""
class AddFaculty(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        try:
            # this if ensure only and admin or a super admin can add a faculty
            if self.request.user.role_id == 1 or self.request.user.role_id == 2:          
                name = request.data.get('name')
                Faculty.objects.create(name=name)
                data = Faculty.objects.filter().values('id', 'name')
                return JsonResponse({'message': 'Faculty added successfully!', 'data': list(data)})
            else:
                return AuthenticationFailed('Cannot add faculty, Not authorized')
        except Exception:
            return JsonResponse({'message': 'Invalid user, Not an admin'})
"""
The AddProgram class creates and adds a new program into the database
"""
class AddProgram(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        try:
            # this if ensure only and admin or a super admin can add a program
            if self.request.user.role_id == 1 or self.request.user.role_id == 2:       
                name = request.data.get('name')
                Program.objects.create(name=name)
                data = Program.objects.filter().values('id', 'name')
                return JsonResponse({'message': 'Program added successfully!', 'data': list(data)})
            else:
                return AuthenticationFailed('Cannot add program, Not authorized')
        except Exception:
            return JsonResponse({'message': 'Invalid user, Not an admin'})
"""
The AddStudent class creates and adds a new student into the database
"""
class AddStudent(APIView):
    def post(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')
        gender = request.data.get('gender')
        role_id = request.data.get('role_id')
        faculty = request.data.get('faculty')
        program = request.data.get('program')
        # this try and catch ensures that a student is not added twice
        try: 
            Student.objects.get(student_id=student_id)           
            raise StudentAlreadyExists

        except Student.DoesNotExist:
            # this try and catch ensures that a student email does not already exist
            try: 
                User.objects.get(email=email, phone_number=phone_number)           
                raise UserAlreadyExist
            except User.DoesNotExist:
                    # this try saves these details in the user model
                    try:
                        details = {                   
                            'first_name' : first_name,
                            'last_name' : last_name,
                            'email' : email,
                            'password' : make_password(password),
                            'phone_number' : phone_number,
                            'gender' : gender,
                            'role_id': role_id,
                        }  
                        # this validates user input
                        validation_response = validate_user_input(email, first_name, last_name, password)        
                        if validation_response is not None:
                            return validation_response
                        else:
                            # this try saves these details in the student model
                            try:                   
                                UserRole.objects.get(id=role_id)
                                # user details are saved here
                                user = User.objects.create(**details)               
                                faculty = Faculty.objects.create(name=faculty)
                                program = Program.objects.create(name=program)
                                student_details = {
                                    'student_id' : student_id,
                                    'user' : user,
                                    'faculty' : faculty,
                                    'program' : program,
                                }  
                                # student details are saved here
                                Student.objects.create(**student_details)           
                                data = User.objects.filter().values()
                                return JsonResponse({'message': 'Student created successfully', 'data':list(data)})
                            except UserRole.DoesNotExist:
                                return JsonResponse({'message': 'Role id is incorrect', 'data': role_id})
                    except Exception as e:
                        print(e)
                        return JsonResponse({'message': 'Invalid credentials, Unable to add student'})

"""
The Login class allows both student and admins to login to the system
"""
class Login (APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password =  request.data.get('password')  
         # this validates user input
        validation_response = validate_login_user_input(email, password)        
        if validation_response is not None:
            return validation_response
        else: 
            try:
                user = User.objects.get(email=email)
                 # this validates user password
                if (user.check_password(password)):                    
                    refresh = RefreshToken.for_user(user)
                    new_user = Student.objects.filter(user__email=email).values()
                    # this gives the user their access and refresh token
                    data ={                                         
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    }
                    return JsonResponse({'message': 'Login successfully', 'data': data, 'user': new_user[0]})
                else:
                    raise InvalidPassword('Invalid password')
            except User.DoesNotExist:
                raise WrongCredentials('Invalid credentials, Wrong user!')

"""
The GetUserRole class displays all the user roles in the system
"""
class GetUserRole(APIView):
    def get(self, request, *args, **kwargs):
        data = UserRole.objects.filter().values("id","name")
        
        return JsonResponse({'message': 'Success', 'data':list(data)})
    
"""
The GetAllStudents class displays all the students  in the system
"""
class GetAllStudents(APIView):
    def get(self, request, *args, **kwargs):
        data = Student.objects.filter().values("id","user", "student_id", "user__first_name", "user__last_name","user__email", "faculty", "program", "user__gender", )
        
        return JsonResponse({'message': 'Success', 'data':list(data)})