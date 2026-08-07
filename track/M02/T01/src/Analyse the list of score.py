# Read the number of scores
n = int(input())

# Read each score and store it in an empty list using append()
scores = []
for _ in range(n):
    score = int(input())
    scores.append(score)

# Read one score to search for
search_score = int(input())

# Calculate values using max(), min(), and sum()
highest_score = max(scores)
lowest_score = min(scores)
total_score = sum(scores)

# Display results in the exact required output format
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Total Score: {total_score}")

# Display search result using the 'in' operator
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")