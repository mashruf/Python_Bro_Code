name = "Mashruf Mahabub"

# length of a string
print(len(name)) # 15

# find first occurence of a given character
print(name.find(" ")) # 7

# find last occurence of a given character
print(name.rfind("a")) # 11

# capitalize a string
print(name.capitalize()) # Mashruf mahabub

# All uppercase
print(name.upper()) # MASHRUF MAHABUB

# All lowecase
print(name.lower()) # mashruf mahabub

# if a string contains only digits
print(name.isdigit()) # False

# if a string contains only alphabatical character
print(name.isalpha()) # False, if there is space then it False

# count the number of a specific character in a string
print(name.count("M")) # 2

# replace one character with other
print(name.replace(" ", "+")) # Mashruf+Mahabub

# to find all the string function available
help(str)

