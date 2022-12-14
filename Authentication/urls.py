from django.urls import path, include
from Authentication.views import AddStudent, AddFaculty, AddAdmin, AddUserRoles, Login, AddPosition, AddProgram

urlpatterns = [
    path('add-user-role/', AddUserRoles.as_view(), name='add_user_roles'),
    path('add-admin/', AddAdmin.as_view(), name='add_admin'),
    path('add-faculty/', AddFaculty.as_view(), name='add_faculty'),
    path('add-position/', AddPosition.as_view(), name='add_position'),
    path('add-program/', AddProgram.as_view(), name='add_program'),
    path('signup/', AddStudent.as_view(), name='add_student'), 
    path('login/', Login.as_view(), name="Login")  
]