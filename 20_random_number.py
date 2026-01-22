import random

# to know details
# print(help(random))

# random integer 
number = random.randint(1, 6) # random number from 1 to 6
print(number) #2

# we can place variable in the randint method
low = 1
high = 50
num = random.randint(low, high)
print(num) # 35


# random floating point number
num = random.random() # will return a random floating point number from 0 to 1
print(num)

# we can choose random value from a collection
options = ('Rock', 'Paper', 'Scissors')
option = random.choice(options)
print(option) # Rock

# we can also shuffle
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards) # it changes the original collection
print(cards) # ['9', '6', '7', 'Q', '5', '8', '4', 'K', '3', '2', '10', 'J', 'A']
