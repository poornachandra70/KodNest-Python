# Read the number of students
student_count = int(input())

# Initialize variables
total_marks = 0
passed_count = 0
failed_count = 0

# Read and process each mark
for i in range(student_count):
    marks = int(input())
    total_marks = total_marks + marks
    if marks >= 40:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1

# Display the summary
print(f"Total Marks: {total_marks}")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}")

# Display the batch result
if failed_count == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")