from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "super_secret_key"

# محاكاة لقاعدة بيانات الطلاب
students_db = {
    "2021001": {"name": "Eid Oukal", "allowed": True},
    "2021002": {"name": "Ahmed Ali", "allowed": False}
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/check_student', methods=['POST'])
def check_student():
    student_id = request.form.get('student_id')
    
    if student_id in students_db:
        if students_db[student_id]['allowed']:
            return redirect(url_for('start_exam', id=student_id))
        else:
            flash("عذراً، أنت غير مخول بدخول الاختبار حالياً.")
    else:
        flash("رقم الطالب غير موجود.")
    
    return redirect(url_for('login'))

@app.route('/exam/<id>')
def start_exam(id):
    student_name = students_db[id]['name']
    return f"مرحباً {student_name}، يمكنك البدء في الاختبار الآن."

if __name__ == '__main__':
    app.run(debug=True)