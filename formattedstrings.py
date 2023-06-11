first = "John"
last = "Smith"
#string concantination
message = first + " [" + last +"]  is a coder"

#formatted strings
msg = f"{first} [{last}] is a coder"
print(msg)

#count characters using len function - general purpose
course = "Python for Beginners"
print(len(course))
#specific functions for strings are called methods
print(course.upper())
print(course.lower())
print(course.find("B"))
print(course.replace("Beginners", "Absolute Beginners"))
print("for" in course)

