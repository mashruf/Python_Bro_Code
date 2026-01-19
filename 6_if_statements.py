# if = do some code only if some condition is true
# else do something else

age = int(input("Enter your age: "))

# if 
# if age >= 18:
#     print("You are now signed up")

# else
# if age >= 18:
#     print("You are now signed up")
# else:
#     print("You must be 18+ to sign up")


# elif
# if age >= 18:
#     print("You are now signed up")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You must be 18+ to sign up")

# order for elif
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")

# age >= 100 in if block and age >= 18 is in elif block
# because age >= 18 technically right for the condition
# if we enter 101, it is greater than 100 as well as 18
# so we should make the order based on the condition


# with boolean value

for_sale = True

if for_sale:
    print("This item is for sell!") # This item is for sell!
else:
    print("This item is not for sell!")