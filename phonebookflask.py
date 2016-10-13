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
def submit_new_entry():
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

@app.route('/update_entry')
def update_entry():
    idnum = request.args.get('id')
    print idnum
    if not idnum:
        return redirect('/')
    results = db.query('select * from phonebook where id = {0}'.format(idnum)).namedresult()
    contact = results[0]
    return render_template(
        'update_entry.html',
        contact = contact
    )

@app.route('/submit_update_entry', methods=['POST'])
def submit_update_entry():
    idnum = request.form.get('id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    action = request.form.get('action')
    if action == 'save':
        db.update(
            'phonebook',
            id=idnum,
            name=name,
            phone=phone,
            email=email
        )
    else:
        db.delete(
            'phonebook',
            id=idnum
        )
    return redirect('/')

@app.route('/delete_entry')
def delete_entry():
    idnum = request.args.get('id')
    if not idnum:
        return redirect('/')
    db.delete('phonebook', id=idnum)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
