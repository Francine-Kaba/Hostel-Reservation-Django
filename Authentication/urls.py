from django.urls import path, include
from Authentication.views import AddStudent, AddFaculty, AddAdmin, UserRoles

urlpatterns = [
    path('add-user-role/', UserRoles.as_views(), name='add user roles'),
    path('add-admin/', AddAdmin.as_view(), name='add admin'),
    path('add-faculty/', AddFaculty.as_view(), name='add faculty'),
    path('signup/', AddStudent.as_view(), name='add-student'),   
]