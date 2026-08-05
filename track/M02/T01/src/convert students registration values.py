# A student registration system has received some values in data types that are not suitable for their intended use.


age_text = "21"
course_fee_text = "499.50"
attempts = 3
# Convert the values here
age=int(age_text)
course_fee=float(course_fee_text)
attempt_text=str(attempts)
# Display the converted values and their
print(age)
print(type(age))
print(course_fee)
print(type(course_fee))
print(attempt_text)
print(type(attempt_text))