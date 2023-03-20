from create_db.models import db, GroupModel, CourseModel, StudentModel
import random
import string
import names


# Generate test data:


def create_groups():
    groups = []
    for i in range(10):
        name = ''.join(random.choices(string.ascii_uppercase, k=2)) + '-' + \
               ''.join(random.choices(string.digits, k=2))
        group = GroupModel(name=name)
        groups.append(group)
        db.session.add(group)
    return groups


def create_students():
    students = []
    for _ in range(200):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        student = StudentModel(first_name=first_name, last_name=last_name)
        students.append(student)
        db.session.add(student)
    return students


def create_courses():
    courses = []
    for name in ["Math", "Biology", "Chemistry", "Physics", "History", "Art", "Music", "Physical Education",
                 "Computer Science", "English"]:
        course = CourseModel(name=name, description=f"Description for {name}")
        courses.append(course)
        db.session.add(course)
    return courses


def students_in_groups(students, groups):
    for group in groups:
        num_students = random.randint(0, 200)
        group_students = random.sample(students, num_students)
        for student in group_students:
            student.group = group
            db.session.add(student)


def student_in_courses(students, courses):
    for student in students:
        num_courses = random.randint(1, 3)
        student_courses = random.sample(courses, num_courses)
        for course in student_courses:
            student.courses.append(course)
            db.session.add(student)


def create_all_tables():
    students, courses, groups = create_students(), create_courses(), create_groups()

    students_in_groups(students, groups)
    student_in_courses(students, courses)

    db.session.commit()
    db.session.close_all()

