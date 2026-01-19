# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence etc

# 1-10
for x in range(1,11):
    print(x)

# 10-1
for x in reversed(range(1,11)):
    print(x)

# odd number using step
for x in range(1,11,2): # 1 3 5 7 9
    print(x)

# iterate over a string
credit_card = "123-456-789-012"

for x in credit_card:
    print(x)


# continue
for x in range(1,11):
    if x == 5:
        continue
    print(x) # 1 2 3 4 6 7 8 9 10

# break
for x in range(1,11):
    if x == 5:
        break
    print(x) # 1 2 3 4