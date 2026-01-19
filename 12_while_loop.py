# while loop = execute some code WHILE some conditions remain true

name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Your name {name}")

# the above code will end if any of the conditions satisfy

# if we want to continue the code till the user enter his name then we will use while
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # this is to escape the loop. Otherwise the loop will continue infinitely
print(f"Your name is {name}")


# number between 1-10
num = int(input("Enter a number 1-10:"))

while num < 1 or num > 10:
    print("The number is invalid")
    num = int(input("Enter a number 1-10:"))
print(f'You entered number {num}')
