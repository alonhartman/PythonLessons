student_names = ["Mark", "Katarina", "Jessica"]
# print the list elements using a loop
for name in student_names:
    print("Student name is {0}".format(name))

print("\n")
x = 0
print("the value of x is {0}".format(x))
for index in range(10):
    x += 10
    print("the value of x is {0}".format(x))

print("\n")

# range function - range(startPosition, endPosition, incrementBy)
x = 0
for index in range(5, 10, 2):
    x += 10
    print("the value of x is {0}".format(x))

# -------------------
x = 0
while x < 10:
    print("Count is", x)
    x += 1
