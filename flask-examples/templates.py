from flask import Flask, render_template
import pg

db = pg.DB(dbname='student_db')
app = Flask('MyApp')

@app.route('/')
def projects():
    query = db.query('select * from student')

    return render_template(
        'students.html',
        title='Students',
        student_list=query.namedresult())

if __name__ == '__main__':
    app.run(debug=True)
