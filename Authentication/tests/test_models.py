from django.test import TestCase
from Authentication.models import Faculty, User, Position, Student, Program

# Create your tests here.
class StudentModelTest(TestCase):
    last_name = 'Snow'
    faculty_name = 'Example Faculty Name'
    program_name = 'Example Program Name'
    student_id = '*************'
    position_name = 'Student'

    def setUp(self):
        user = User.objects.create(
            first_name='Jon', last_name= self.last_name,
        )
        faculty = Faculty.objects.create(name=self.faculty_name)
        program = Program.objects.create(name=self.program_name)
        Position.objects.create(name=self.position_name)

        student = Student(
            student_id=self.student_id, 
            user=user, 
            faculty=faculty, 
            program=program
        )
        student.save()

    def test_position(self):
        position = Position.objects.get(name=self.position_name)
        self.assertEqual(str(position), self.position_name)

    def test_save_user(self):
        user = User.objects.get(first_name='Jon')
        self.assertEqual(user.last_name, self.last_name)

    def test_program(self):
        program = Program.objects.get(name=self.program_name)
        self.assertEqual(str(program), self.program_name)

    def test_faculty(self):
        faculty = Faculty.objects.get(name=self.faculty_name)
        self.assertEqual(str(faculty), self.faculty_name)

    def test_student_save(self):
        student = Student.objects.get(student_id=self.student_id)
        self.assertEqual(str(student), student.student_id)
    
    