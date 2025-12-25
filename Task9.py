student_marks={"Ram":89,"Shyam":85,"Radha":75,"Alice":85}
name = input("Enter the Student's Name: ")
if name in student_marks:
    print(f"{name}'s Marks: {student_marks[name]}")
else:
    print("Student not found.")