#Prompt the user to enter the total number of students in the class. 
students = int(input("Enter the total number of students in the class: "))
#Prompt the user to enter the total number of periods of the class held in the week (between 1 and 5).
periods = int(input("Enter total number of periods of the class held in the week (between 1 and 5): "))
names = []
attendance = []
#For each student, prompt the user to enter the student's name.
#For each student, prompt the user to enter attendance for each period
for i in range(students):
    name = input(f"Enter name for student {i + 1} name: ")
    names.append(name)
    student_attendance = []
    for j in range(periods):
        mark = input(f"Enter attendance for {name} (P/A) for period {j + 1}: ").upper()
        student_attendance.append(mark)
    attendance.append(student_attendance)
    
#Calculate the total number of classes each student was present for and the attendance percentage for each student.
#Display each student's name, total days present, and attendance percentage. Include a warning for students with attendance below 75%. 
print("\n--- Attendance Report ---")
for i in range(students):
    present = attendance[i].count('P')
    percent = (present / periods) * 100
    print(f"{names[i]}: {present}/{periods} Present ({percent:.0f}%)")
    if percent < 75:
        status= ("-WARNING: Low attendance!")

#Store the student names and daily attendance records in a file.
with open("attendance.txt", "w") as f:
    for i in range(students):
        f.write(f"{names[i]}: {', '.join(attendance[i])}\n")

print("\nSaved to 'Data File'")