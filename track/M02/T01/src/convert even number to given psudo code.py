# Convert Even-Number Sum
# Pseudocode to Python
# During Foundation Month, you learned
#to represent a solution using pseudocode.
# Convert the following pseudocode into an executable Python program without
#changing its logic.
#The program must read a positive
#integer limit , examine every number
#from 1 to limit , add the display the even numbers and total


# Read the limit
limit = int(input())
number = 1
total = 0
while number<=limit:
    if number % 2 == 0:
        total = total + number
    number = number + 1
print(f"Even Sum: {total}")