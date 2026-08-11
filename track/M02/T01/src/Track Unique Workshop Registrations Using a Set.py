n = int(input())
registration = set()
total_entries = 0

for _ in range(n):
    registration.add(input())
    total_entries += 1
    
    registrations.add(students_id)

search_id = input().strip()
unique_count = len(registration)
duplicate_count = total_entries - uniques_count

print(f"Unique Registration: {unique_count}")
print(f"Duplicaate Entries: {duplicate_count}")

if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")
