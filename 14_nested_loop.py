# nested loop = a loop within another loop(outer, inner)
# outer loop:
#    inner loop:

# for y in range(1, 10):
#     print(y, end="")  # end="" will print result in the same line. We can also use any symbol or space in place of "".


# to run the above loop three time, we will create an outer loop

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()