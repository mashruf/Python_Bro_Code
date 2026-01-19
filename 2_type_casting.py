# the process of converting a variable from one data type to another
# str(), int(), float(), bool()
# type casting is specially useful for handling user input
# user input is always string
# we will get cases where we need to convert a variable to another data type

name = "Rohon"
age = 20
gpa = 3.2
is_student = True

# to get the type of a variable we use type()
print(type(name)) # <class 'str'>

# int to float
print(float(age)) # 20.0

# float to int
print(int(gpa)) # 3

# bool
print(bool(name)) # True, because the string is not empty


