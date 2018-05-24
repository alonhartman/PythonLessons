students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


# student_id has a default value so the user doesn't have to send a value when calling the method
# if the user wants to overwrite the default value, he should send the value when he calls the method
def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


student_list = get_students_titlecase()
add_student("Mark", 15)


# definition of a function that receives 1 'name' parameter and a '*args' parameter
# the *args parameter can get multiple parameters and from different types
def var_args(name, *args):
    print("\nvar_args")
    print(name)
    print(args)


var_args("Mark", "love python", None, "Hello", True)


#
#
def var_args2(name, **kwargs):
    print("\nvar_args2")
    print(name)
    print(kwargs["description"], kwargs["feedback"])


var_args2("Mark", description="loves python", feedback=None, pluralsight_subscriber=True)
