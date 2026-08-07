name = input()
course = input()
score = int(input())

# Create the tuple
student_record = (name, course, score)

# Unpack the tuple
u_name, u_course, u_score = student_record

# Display the unpacked values
print(f"Name: {u_name}")
print(f"Course: {u_course}")
print(f"Score: {u_score}")