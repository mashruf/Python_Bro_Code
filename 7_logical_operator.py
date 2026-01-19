# logical operator =  evaluates multiple condition(or, and, not)
# or = atleast one condition must be true
# and = both condition must be true
# not = inverts the condition(not False, not True)

# or
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled") # The outdoor event is still scheduled


# and
temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside") 
    print("It is sunny") 
elif 28 > temp > 0 and is_sunny: # 28 > temp > 0 = temp < 28 and temp > 0
    print("It is warm outside")
    print("It is sunny")



# not
age = 19
is_male = True


if age > 18 and not is_male:
    print("You are able to participate") 
else:
    print("You are not able to participate") # You are able to participate

# is_male = True
# not is_male = False
# is_male is converted to False for using not