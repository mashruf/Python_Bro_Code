# collection = single variable used to store multiple value
# list = [], ordered and changeable. duplicate ok
# set = {}, unordered and immutable, but add/remove ok. no duplicate
# tuple = (), ordered and unchangeable. duplicates ok. faster


# we can use index operator over collection just like string

# list
fruits = ['apple', 'orange', 'banana', 'coconut']

# access an element
print(fruits[2]) # banana

# print first 3 fruits
print(fruits[:3]) # ['apple', 'orange', 'banana']

# every second element
print(fruits[::2]) # ['apple', 'banana']

# backward
print(fruits[::-1]) # ['coconut', 'banana', 'orange', 'apple']

# iterate over collection
for fruit in fruits:
    print(fruit, end=" ") # apple orange banana coconut
print()

# to know the avalaible built in method for a list
# print(dir(fruits))

# to know the details of the built in methods
# print(help(fruits))

# list method

# length of a collection
print(len(fruits)) # 4

# find if a value in a collection
print("apple" in fruits) # True

# change value of a list
fruits[0] = "strawberry"
print(fruits) # ['strawberry', 'orange', 'banana', 'coconut']


# add new element to a list
fruits.append("grape")
print(fruits) # ['strawberry', 'orange', 'banana', 'coconut', 'grape']

# remove an element
fruits.remove("strawberry")
print(fruits) # ['orange', 'banana', 'coconut', 'grape']

# add value in a given index
fruits.insert(0, "jackfruit")
print(fruits) # ['jackfruit', 'orange', 'banana', 'coconut', 'grape']

# sort a list
fruits.sort()
print(fruits) # ['banana', 'coconut', 'grape', 'jackfruit', 'orange']

# reverse a list
fruits.reverse()
print(fruits) # ['orange', 'jackfruit', 'grape', 'coconut', 'banana']

# return index of an element
print(fruits.index("orange")) # 0

# count occurance of a specific element
print(fruits.count("grape")) # 1

# clear a list
fruits.clear()
print(fruits) # []

# set
fruits = {'apple', 'orange', 'banana', 'coconut'}

# iterable like list by for loops

# unordered
print(fruits) # {'banana', 'apple', 'orange', 'coconut'}

# to know the avalaible built in method for a set
# print(dir(fruits))

# to know the details of the built in methods
# print(help(fruits))

# length
print(len(fruits)) # 4

# if a value in a set
print("orange" in fruits) # True

# add element in a set
fruits.add("pineapple")
print(fruits) # {'orange', 'apple', 'banana', 'coconut', 'pineapple'}

# remove an element
fruits.remove("orange")
print(fruits) # {'apple', 'pineapple', 'banana', 'coconut'}

# remove first element from a set. Though the set will be random every time
fruits.pop()
print(fruits) # {'banana', 'apple', 'pineapple'}

# clear a se
fruits.clear()
print(fruits) # set()


# tuple
fruits = ('apple', 'orange', 'banana', 'coconut')

# iterable like list by for loops

# to know the avalaible built in method for a tuple
# print(dir(fruits))

# to know the details of the built in methods
# print(help(fruits))

# length 
print(len(fruits)) # 4

# find if a value in a tuple
print("banana" in fruits) # True

# index of an element
print(fruits.index("banana")) # 2

# count occurence of an element
print(fruits.count("banana")) # 1