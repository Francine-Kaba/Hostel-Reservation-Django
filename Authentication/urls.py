from django.urls import path, include
from Authentication.views import (AddStudent, AddFaculty, AddAdmin,
AddUserRoles,Login, AddPosition, AddProgram, GetUserRole, GetAllStudents, GetFaculties, GetPositions)

urlpatterns = [
    path('user-role', AddUserRoles.as_view(), name='add_user_roles'),
    path('admin', AddAdmin.as_view(), name='add_admin'),
    path('faculty', AddFaculty.as_view(), name='add_faculty'),
    path('position', AddPosition.as_view(), name='add_position'),
    path('program', AddProgram.as_view(), name='add_program'),
    path('signup', AddStudent.as_view(), name='signup'),
    path('login', Login.as_view(), name="Login"),
    # gets
    path('all-user-role', GetUserRole.as_view(), name="all-user-role"),
    path('all-students', GetAllStudents.as_view(), name="get-all-students"),
    path('all-faculties', GetFaculties.as_view(), name="get-all-faculties"),
    path('all-positions', GetPositions.as_view(), name="get-all-positions"),
]
