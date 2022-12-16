from django.urls import path, include
from Authentication.views import AddStudent, AddFaculty, AddAdmin, AddUserRoles, Login, AddPosition

urlpatterns = [
    path('add-user-role/', AddUserRoles.as_view(), name='add user roles'),
    path('add-admin/', AddAdmin.as_view(), name='add admin'),
    path('add-faculty/', AddFaculty.as_view(), name='add faculty'),
    path('add-position/', AddPosition.as_view(), name='add position'),
    path('signup/', AddStudent.as_view(), name='add-student'), 
    path('login/', Login.as_view(), name="Login")  
]