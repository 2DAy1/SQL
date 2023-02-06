import random
import string
import names


def get_groups():
    groups = []
    for _ in range(10):
        letters = ""
        numbers = 0
        for _ in range(2):
            letters += random.choice(string.ascii_letters)
            numbers += random.randint(0, 10)
        groups.append(f"{letters}{numbers}")


def get_students():
    return [names.get_full_name() for _ in range(200)]


def students_in_groups(students:list, groups:list):
    ful_groups = {}
    for group in groups:
        ful_groups[group] = [student for student in students ]
