def display_student(name, course, level):
    print(f"{name} | {course} | {level}")

# positional argument
display_student("Aarav", "Python", "Beginner")
# keyword argument
display_student(name="Meera", course="Java", level="Intermediate")
# mixed argument
display_student("Kabir", course="SQL", level="Beginner")