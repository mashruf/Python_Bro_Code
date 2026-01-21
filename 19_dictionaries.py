# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates.

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# to know the method of dict
# print(dir(capitals))

# in depth about the methods
# print(help(capitals))

# get the value of a key
print(capitals["USA"])

# or

print(capitals.get("India"))

# if a value is not in the dictionary
print(capitals.get("Japan")) # None, works only by get

# add new key value pair
capitals["Japan"] = "Tokyo"
print(capitals) # {'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Japan': 'Tokyo'}


# or we can use the update method
capitals.update({"Bangladesh": "Dhaka"})
print(capitals)

# we can update an existing key value pair
capitals.update({"USA": "Newyork"})
print(capitals)


# remove key value pair
capitals.pop("China")
print(capitals)

# remove latest key value pair
capitals.popitem()
print(capitals)


# get all the keys
keys = capitals.keys()
print(keys) # dict_keys(['USA', 'India', 'Russia', 'Japan'])

#get all the values
values = capitals.values()
print(values) # dict_values(['Newyork', 'New Delhi', 'Moscow', 'Tokyo'])

# we can iterate over keys and values
for key in keys:
    print(key) # we will get all values separately

# we can get both key value pair
items = capitals.items()
print(items) # dict_items([('USA', 'Newyork'), ('India', 'New Delhi'), ('Russia', 'Moscow'), ('Japan', 'Tokyo')])

# we can iterate the items
for key, value in items:
    print(f"{key}:{value}")

# clear dict
capitals.clear()
print(capitals) # {}