from flask import Flask, render_template,request,redirect
import pg

app = Flask('PhonebookApp')
db = pg.DB(dbname='phonebook2')

@app.route('/')
def phonebook():
    query = db.query('select * from phonebook')
    entries = query.namedresult()
    return render_template(
        'phonebook.html',
        title = 'PHONEBOOK',
        results = entries
    )

@app.route('/new_entry')
def new_entry():
    return render_template(
        'new_entry.html',
        title="Add Entry"
    )

@app.route('/submit_new_entry', methods=['POST'])
def submit_entry():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    db.insert(
        'phonebook',
        name=name,
        phone=phone,
        email=email
    )
    return redirect('/')

@app.route('/edit_entry')
def edit_entry():
    return render_template(
        'edit_entry.html',
        title="Add Entry"
    )

@app.route('/change_entry', methods=['POST'])
def change_entry():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    db.insert(
        'phonebook',
        name=name,
        phone=phone,
        email=email
    )
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
