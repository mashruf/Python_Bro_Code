# conditional expression = a one-line shortcut for the if-else statement(ternary operator)
# print or assign one of two values based on a condition
# X if condition else Y


num = 5
print("Positive" if num > 0 else "Negative") # Posiitive

num = 6
result = "EVEN" if num%2 == 0 else "ODD"
print(result) # EVEN

a = 6
b = 7
max_num = a if a>b else b
print(max_num) # 7