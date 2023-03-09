from .models import db, GroupModel, CourseModel, StudentModel
import random
import string
import names



# Generate test data:


def create_groups():
    groups = []
    for i in range(10):
        name = ''.join(random.choices(string.ascii_uppercase, k=2)) + '-' +\
               ''.join(random.choices(string.digits, k=2))
        group = GroupModel(name=name)
        groups.append(group)
    return groups


def create_students():
    students = []
    for _ in range(200):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        student = StudentModel(first_name=first_name, last_name=last_name)
        students.append(student)
    return students


def generate_courses():
    courses = []
    for name in ["Math", "Biology", "Chemistry", "Physics", "History", "Art", "Music", "Physical Education",
                 "Computer Science", "English"]:
        course = CourseModel(name=name, description=f"Description for {name}")
        courses.append(course)
    return courses




def students_in_groups():
    groups = create_groups()
    students = create_students()
    for group in groups:
        num_students = random.randint(10, 30)
        group.students = random.sample(students, num_students)
        for student in group.students:
            student.group = group
    return groups

def create_all_tables():
    students_in_groups()
    generate_courses()

if __name__ == "__main__":
    for i in students_in_groups():
        print(i)

