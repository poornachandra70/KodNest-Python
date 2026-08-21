class StudentProfile:
    # Create the class-level object counter
    profile_count = 0

    def __init__(self, name):
        # Store the name
        self.name = name
        # Increase the shared counter
        StudentProfile.profile_count += 1


n = int(input())
students = []

# Read n names and create n StudentProfile objects
for _ in range(n):
    student_name = input().strip()
    student = StudentProfile(student_name)
    students.append(student)

# Print the number of created profiles
print(f"Profiles Created: {StudentProfile.profile_count}")