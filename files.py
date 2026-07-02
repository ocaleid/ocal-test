student_count=int(input("Enter the number of students: "))
with open ("students.csv", "w") as file:
    file.write("Name,Final Grade,Status,Advice\n")
    for i in range(student_count):
        student_name = input(f"Enter the name of student {i+1}: ")
        final_grade = input(f"Enter the final grade of student {i+1}: ")
        file.write(f"{student_name},{final_grade}\n")