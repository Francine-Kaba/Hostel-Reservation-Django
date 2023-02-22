from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Faculty, Program, UserRole, User

# Register your models here.
admin.site.register(UserRole)
admin.site.register(Faculty)
admin.site.register(Program)
admin.site.register(Student)
