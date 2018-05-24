# define a list
student_names = ["Mark", "Katarina", "Jessica"]
print(student_names[0])

print(student_names[-1])  # will print the length-1 position = Jessica
print(student_names[-2])  # will print the length-2 position = Katarina

# change Mark with James
student_names[0] = "James"
print(student_names[0])


# Add an item to the end of the list
student_names.append("Homer")
print(student_names)

# should print False because Mark was already been replaces with James
print("Mark" in student_names)

# how many elements in the list?
print("the length of the list is: {0}".format(len(student_names)))

# deleting an element from the list
del student_names[2]
print(student_names)

# list slicing
print("before slicing: {0}".format(student_names))
print("after slicing with [1:] {0}".format(student_names[1:]))  # ignored the first element in the [0] position
print("after slicing with [1:-1] {0}".format(student_names[1:-1]))  # ignored the first and last elements of the list


