# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_card_number = "1234-5678-901234"

# first element of the string
print(credit_card_number[0]) # 1

# first 4 digit of the string
print(credit_card_number[0:4]) # 1234
# or
print(credit_card_number[:4]) # 1234

# second 4 digit
print(credit_card_number[5:9]) # 5678

# from a specific index to rest of the digits
print(credit_card_number[5:]) # 5678-901234

# last digit
print(credit_card_number[-1]) # 4

# second last digit
print(credit_card_number[-2]) # 3

# last 4 digits of the credit cart
print(credit_card_number[-4:]) # 1234


# count every second character
print(credit_card_number[::2]) #13-68913

# count every 3rd character
print(credit_card_number[::3]) # 146-14

# reverse a string
print(credit_card_number[::-1])

# count every second character from reverse
print(credit_card_number[::-2])