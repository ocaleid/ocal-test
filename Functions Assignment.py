def calculate_final_grade(attendance, homework, quiz, participation):
    total =(attendance * 0.2) + (homework * 0.35) + (quiz * 0.35) + (participation * 0.1)
    return total

def get_student_status(final_grade, attendance):
    if attendance < 50:
        return ("Failed because of low attendance :(")
    elif final_grade >= 85:
        return ("Excellent :D")
    elif final_grade >= 70:
        return ("Good :)")
    elif final_grade >= 50:
        return ("Needs Improvement :(")
    else:
        return ("Failed :( ")
    
def get_student_advice(attendance, homework, quiz, participation):
    if attendance < 50:
        return ("You need to attend more sessions.")
    elif homework < 50:
        return ("You need to focus more on homework.")
    elif quiz < 50:
        return ("You need to study more for quizzes.")
    elif participation < 50:
        return ("Try to participate more during sessions.")
    else:
        return ("Keep up the good work.")

def print_student_report(name, final_grade, status, advice):
    print("******************************")
    print("Student Report")
    print(f"Name: {name}")
    print(f"Final Grade: {final_grade}")
    print(f"Status: {status}")
    print(f"Advice: {advice}")
    print("******************************")
    
    
def get_valid_score(text):
    while True:
        score = float(input(f"Enter {text} score: "))
        if 0 <= score <= 100:
            return score
        else:
            print(f"Invalid {text} score. Please enter a number between 0 and 100.")
            
   
def get_valid_students_number():
    while True:
        student_count=int(input("How many students do you want to evaluate? "))
        if student_count > 0:
            return student_count
        else:
            print("Invalid number. Please enter a number greater than 0.")
                
    
student_count=get_valid_students_number()

for i in range(student_count):
    print(f"Student {i+1}")
    student_name = input("Enter student name: ")
    attendance = get_valid_score("attendance")
    homework = get_valid_score("homework")
    quiz = get_valid_score("quiz")
    participation = get_valid_score("participation")

    final_grade = calculate_final_grade(attendance, homework, quiz, participation)
    status = get_student_status(final_grade, attendance)
    advice = get_student_advice(attendance, homework, quiz, participation)
    
    print_student_report(student_name, final_grade, status, advice)
