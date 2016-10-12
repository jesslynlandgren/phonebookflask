# the Flask class from the flask module
from flask import Flask

import pg
db = pg.DB(dbname='student_db')

app = Flask('MyApp')

@app.route('/')
def home():
    # Query the database
    query = db.query('select * from student')
    # built up the HTML for a list of projects and send it back
    # to the browser
    html = '<ul>'
    for student in query.namedresult():
        html += '<li>%s</li>' % student.name
    html += '</ul>'
    return html

# Start the server if this file is run as a script on the command line
if __name__ == '__main__':
    # run the server in debug mode, which will automatically
    # restart the server for you on save
    app.run(debug=True)
