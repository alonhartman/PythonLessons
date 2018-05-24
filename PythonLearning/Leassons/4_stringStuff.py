# a String declaration
name = "alon"
name2 = 'hartman'

# useful String methods
print(name.capitalize())  # == Alon
print(name2.replace("a", "e").capitalize())  # == Hertman
print(name.isalpha())
print("123".isdigit())
print("alon,hartman,split,into,array Like".split())

print("nice to meet you {0} {1}.".format(name.capitalize(), name2.capitalize()))
