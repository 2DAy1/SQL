import random
import string
import names


def get_groups():
    groups = []
    for _ in range(10):
        letters = ""
        numbers = ""
        for _ in range(2):
            letters += random.choice(string.ascii_letters).upper()
            numbers += str(random.randint(0, 9))
        groups.append(f"{letters}{numbers}")
    return groups


def get_students():
    return [names.get_full_name() for _ in range(200)]


def get_random_list(l):
    random_items_list = []
    for i in range(random.randint(0, 3)):
        random_items_list.append(l[i])
        del l[i]
    return l, random_items_list


def students_in_groups(students: list, groups: list):
    ful_groups = {}
    groups, empty_groups =get_random_list(groups)
    for group in groups:
        students_list = []
        if students:
            for _ in range(random.randint(10, 30)):
                student = students[random.randint(0, len(students)-1)]
                students_list.append(student)
                students.remove(student)
        ful_groups[group] = students_list
    if students:
        print(students)
    print(empty_groups)
    return ful_groups


for i in students_in_groups(get_students(), get_groups()).items():
    print(i)
