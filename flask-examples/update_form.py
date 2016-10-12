# Now we also need the request object
# Also using redirect
from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='student_db')

app = Flask('MyFormApp')

@app.route('/')
def list():
    student_list = db.query('select * from student').namedresult()
    return render_template(
        'students.html',
        title='Students',
        student_list=student_list
    )

@app.route('/update_student')
def update_student_form():
    id = request.args.get('id')
    if not id:
        return redirect('/')
    sql = 'select * from student where id = %s' % id
    print sql
    result_list = db.query(sql).namedresult()
    student = result_list[0]
    return render_template(
        'update_student.html',
        title='Update Student',
        student=student)

@app.route('/submit_update_student', methods=['POST'])
def submit_form():
    id = request.form.get('id')
    name = request.form.get('name')
    website = request.form.get('website')
    github_username = request.form.get('github_username')
    db.update(
        'student', {
            'id': id,
            'name': name,
            'website': website,
            'github_username': github_username
        })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
