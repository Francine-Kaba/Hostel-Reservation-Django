from django.contrib import admin
from .models import Student, Faculty, Program, UserRole

# Register your models here.
admin.site.register(UserRole)
admin.site.register(Faculty)
admin.site.register(Program)
admin.site.register(Student)
