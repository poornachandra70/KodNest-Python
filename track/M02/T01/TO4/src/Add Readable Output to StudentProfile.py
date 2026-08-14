class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        # Initialize the student attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        # Return the complete formatted profile string
        skills_str = ", ".join(self.skills)
        return f"STUDENT PROFILE\nStudent ID: {self.student_id}\nName: {self.name}\nCourse: {self.course}\nExperience in Years: {self.experience}\nSkills: {skills_str}"

# Read the inputs for student ID, name, course, experience, and skills
student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Display the object using print(student)
print(student)