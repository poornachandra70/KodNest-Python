# Analyze Entered Numbers
 # A number analyzer examines a group of entered values and produces a summary.
 #Write a Python program that first reads how many numbers will be entered.
 #Then read each number one at a time and determine whether it is positive,
 #negative or zero.

number_count = int(input())
positive_count = 0
negative_count = 0
zero_count = 0
for i in range(number_count):
    number = int(input())
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1
print(f"Positive: {positive_count}")
print(f"Negative: {negative_count}")
print(f"Zero: {zero_count}")