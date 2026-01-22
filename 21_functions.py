# function = a block of reusable code
# place () after function name to invoke it

def display_invoice(username, amount, due_date): # these are called parameter
    print(f"Hello {username}!")
    print(f"Your bill is of amount {amount:.2f} is due: {due_date}")

# We are passing argument. We must pass arguments same as the number of parameters.
display_invoice("Rohon", 39.85, "01/02") # Hello Rohon!
                                         # Your bill is of amount 39.85 is due: 01/02




# return = statement used to end a function
# and send a result back to the caller

def add(x, y):
    z = x+y
    return z

print(add(1, 3)) # 4


def create_name(first_name, last_nane):
    first_name = first_name.capitalize()
    last_nane = last_nane.capitalize()

    return f"{first_name} {last_nane}"

name = create_name("mashruf", "mahabub")
print(name) # Mashruf Mahabub