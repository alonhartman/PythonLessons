# a String declaration
name = "alon"
number = "1234"


if name.isalpha():
    print("name is alphanumeric")
else:
    print("name is not alphanumeric")

if number.isdigit():
    print("number is digits")


python_course = True
if python_course:
    print("this will execute")

aliens_found = None
if aliens_found:
    print("this will not execute")
else:
    print("the else did execute")


number = 5
if number != 5:
    print("this will not execute")


a = 1
b = 2
print("Bigger" if a > b else "Smaller")
