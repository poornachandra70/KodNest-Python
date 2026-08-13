# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student_profile(self, profile):
        self.students.append(profile)

    def filter_students_by_course(self, target_course):
        matching_students = []
        for student in self.students:
            if student.course.strip().lower() == target_course.strip().lower():
                matching_students.append(student)
        return matching_students


# Read the student details
n = int(input())

manager = PlacementManager()

for _ in range(n):
    student_id = int(input())
    name = input()
    course = input()
    profile = StudentProfile(student_id, name, course)
    manager.add_student_profile(profile)

filter_course = input()

# Filter and display the matching students
matched_students = manager.filter_students_by_course(filter_course)

if matched_students:
    for student in matched_students:
        print(student)
else:
    print(f"No students found for course: {filter_course}")