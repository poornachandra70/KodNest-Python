# Read marks, attendance and project com
Marks= int(input())
Attendence= int(input())
Project_completion= input()
# Check the academic requirements
if (Marks >=60) and (Attendence>=75):
    if Project_completion == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")

