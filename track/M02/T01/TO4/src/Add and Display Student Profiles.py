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
        # Add the received student object
        self.student_profiles.append(student_profile)

    def display_student_profiles(self):
        # Handle an empty collection
        if not self.student_profiles:
            print("No student profiles available")
        else:
            print("STUDENT PROFILES")
            # Display all stored student profiles
            for profile in self.student_profiles:
                print(profile)


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

manager.display_student_profiles()