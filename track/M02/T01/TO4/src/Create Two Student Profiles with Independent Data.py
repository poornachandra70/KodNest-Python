class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance variables
        self.student_id = student_id
        self.name = name
        self.course = course

# Read the ID, name, and course of the first student
first_id = int(input())
first_name = input().strip()
first_course = input().strip()

# Read the ID, name, and course of the second student
second_id = int(input())
second_name = input().strip()
second_course = input().strip()

# Create the first StudentProfile object
student1 = StudentProfile(first_id, first_name, first_course)

# Create the second StudentProfile object
student2 = StudentProfile(second_id, second_name, second_course)

# Print the data stored in both objects in the required format
print(f"Student 1\nID: {student1.student_id}\nName: {student1.name}\nCourse: {student1.course}")
print(f"Student 2\nID: {student2.student_id}\nName: {student2.name}\nCourse: {student2.course}")