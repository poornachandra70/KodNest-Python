class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def find_student_by_id(self, student_id):
        # Search for and return the matching object
        for student in self.student_profiles:
            if student.student_id == student_id:
                return student
        # Return None if no match is found
        return None


# Read the number of students
n = int(input())

manager = PlacementManager()

# Read student details and add them to the manager
for _ in range(n):
    student_id = int(input())
    name = input()
    course = input()
    profile = StudentProfile(student_id, name, course)
    manager.add_student_profile(profile)

# Read the search ID
search_id = int(input())

# Search for the student profile
result = manager.find_student_by_id(search_id)

# Display the output as per requirements
if result:
    print(result)
else:
    print(f"Student profile with ID {search_id} not found")