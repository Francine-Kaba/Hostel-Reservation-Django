from django.urls import path, include
from Authentication.views import AddStudent

urlpatterns = [
    path('signup/', AddStudent.as_view(), name="add-student"),

]