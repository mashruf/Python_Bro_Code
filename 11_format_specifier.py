# format specifier = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center allign
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive number
# :, = comma seperator


price1 = 3.14159
price2 = -987.65
price3 = 12.34

# decimal point precision
print(f"Price 1 is {price1:.2f}") # Price 1 is 3.14
print(f"Price 2 is {price2:.2f}") # Price 2 is -987.65
print(f"Price 3 is {price3:.2f}") # Price 3 is 12.34

# allocate that many spaces
print(f"Price 1 is {price1:10}") # Price 1 is ...3.14159 ,(3 leading spaces + 7 characters = 10 total)
print(f"Price 2 is {price2:10}") # Price 2 is ...-987.65
print(f"Price 3 is {price3:10}") # Price 3 is .....12.34

# allocate that many spaces with 0
print(f"Price 1 is {price1:010}") # Price 1 is 0003.14159 ,(3 leading 0 + 7 characters = 10 total)
print(f"Price 2 is {price2:010}") # Price 2 is 000-987.65
print(f"Price 3 is {price3:010}") # Price 3 is 0000012.34

# left justify
print(f"Price 1 is {price1:<10}") # Price 1 is 3.14159...   
print(f"Price 2 is {price2:<10}") # Price 2 is -987.65...   
print(f"Price 3 is {price3:<10}") # Price 3 is 12.34.....

# center align
print(f"Price 1 is {price1:^10}") # Price 1 is  3.14159
print(f"Price 2 is {price2:^10}") # Price 2 is  -987.65
print(f"Price 3 is {price3:^10}") # Price 3 is   12.34

# use a plus sign to indicate positive value
print(f"Price 1 is {price1:+}") # Price 1 is +3.14159
print(f"Price 2 is {price2:+}") # Price 2 is -987.65
print(f"Price 3 is {price3:+}") # Price 3 is +12.34

# insert a space before positive number
print(f"Price 1 is {price1: }") # Price 1 is .3.14159
print(f"Price 2 is {price2: }") # Price 2 is -987.65
print(f"Price 3 is {price3: }") # Price 3 is .12.34

# comma seperator
price1 = 3000000.14159
price2 = -9870000.65
price3 = 12000.34

print(f"Price 1 is {price1:,}") # Price 1 is 3,000,000.14159
print(f"Price 2 is {price2:,}") # Price 2 is -9,870,000.65
print(f"Price 3 is {price3:,}") # Price 3 is 12,000.34


# combination of specifier
print(f"Price 1 is {price1:+,.2f}") # Price 1 is +3,000,000.14
print(f"Price 2 is {price2:+,.2f}") # Price 2 is -9,870,000.65
print(f"Price 3 is {price3:+,.2f}") # Price 3 is +12,000.34
