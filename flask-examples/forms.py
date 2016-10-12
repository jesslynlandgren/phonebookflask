# Now we also need the request object
# Also using redirect
from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='student_db')

app = Flask('MyFormApp')

@app.route('/')
def new_student_form():
    return render_template(
        'new_student.html',
        title='New Student')

@app.route('/submit_new_student', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    website = request.form.get('website')
    github_username = request.form.get('github_username')
    db.insert(
        'student',
        name=name,
        website=website,
        github_username=github_username)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
