import random
import string
import names


def create_groups():
    groups = []
    for _ in range(10):
        letters = ""
        numbers = ""
        for _ in range(2):
            letters += random.choice(string.ascii_letters).upper()
            numbers += str(random.randint(0, 9))
        groups.append(f"{letters}{numbers}")
    return groups


def create_students():
    return [names.get_full_name() for _ in range(200)]


def create_courses():
    return ['Math', 'Biology', 'Chemistry', 'Physics', 'History', 'Geography', 'Literature', 'Art', 'Music',
            'Computer Science']

def asign_students_courses(students: list, courses):
    student_courses = {}
    for student in students:
        num_courses = random.randint(1, 3)
        courses_assigned = random.sample(courses, num_courses)
        student_courses[student] = courses_assigned
    return student_courses


def students_in_groups(students: dict, groups: list):
    group_assignments = {}
    for student in students:
        group = random.choice(groups)
        if group not in group_assignments:
            group_assignments[group] = {}
        group_assignments[group][student] = students[student]
    return group_assignments





students = asign_students_courses(create_students(), create_courses())
groups = students_in_groups(students,create_groups())
print(students)
print(groups)


