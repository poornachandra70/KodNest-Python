# Analyze Multiples of Three
# Write a Python program that reads a limit and a target number
limit = int(input())
target = int(input())
count = 0
total = 0
found = False
for i in range(1,limit+1):
    # Examine every number from 1 to the limit
    if i % 3 ==0:
        # Check if multiple of 3
        total +=i
        count +=1
        if i == target:
            found = True
# Display the count, total and search result
print("Count:",count)
print("Sum:",total)
if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")
