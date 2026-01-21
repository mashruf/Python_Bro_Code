# 2d list = a list made up of lists

fruits = ['apple', 'orange', 'banana']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

# 2d list
groceries = [fruits, vegetables, meats]

# print 2d list
print(groceries) # [['apple', 'orange', 'banana'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

# print specific element of a 2d list
print(groceries[0]) # ['apple', 'orange', 'banana']


# accessing element of an list from the 2d list
print(groceries[0][2]) # banana


# to iterate over a 2d list we can use for loop
for collection in groceries:
    print (collection) # ['apple', 'orange', 'banana']
                       # ['celery', 'carrots', 'potatoes']
                       # ['chicken', 'fish', 'turkey']


# to iterate every list inside a 2d list we have to use nested loop
for collection in groceries:
    for x in collection:
        print(x, end = " ")
    print()
# apple orange banana 
# celery carrots potatoes 
# chicken fish turkey 


# like list we can have list of tuple, tuple of tuple, tuple of set etc