#Command Line Phonebook App

##Summary:
This project is a webapp for a locally hosted SQL phonebook database.  The entries in the phonebook consist of a name key connected to 2 pieces of info: a phone number and an email address.  The site provides a friendly web-based interface for the phonebook.

This project was completed as part of the Python curriculum for Digital Crafts

##Github Link
[Phonebook Flask](https://github.com/jesslynlandgren/phonebookflask)

##What was used:
* Python 2.7.12 (Including the following modules):
  - PyGreSQL
* Flask/Jinja
* PostGreSQL locally hosted database
* HTML/CSS
* Bootstrap
  - (Bootswatch Darkly theme)

##Requirements:
(Cannot be run - database is currently hosted locally)
* Python 2 or Python 3
* Flask/Jinja

##Goals:
Create a web application for an existing SQL phonebook database similar to [Phonebook Obj](https://github.com/jesslynlandgren/phonebook_obj)
* Each page should extend a base HTML template.  There should be a main page and then separate pages for editing a contact or creating a new contact.
* Default page should list all current phonebook entries
* Each entry listing should have an option for editing or deleting that entry
* Adding a new entry or updating an entry should be done via a form that pre-populates with current entry information

##Code Snippets
All pages were built off of a "layout.html" template.  The layout template contains the necessary header, styling, and top bar elements.  The remaining pages overwrite a div element in that template with the entry list or appropriate table.

```html
{% extends 'layout.html' %}

{% block body %}
  <h2 class="contacts">Contacts</h2>
    <table class="table table-striped table-responsive">
      <thead>
        <tr>
          <th class="text-success">Name</th>
          <th class="text-warning">Phone Number</th>
          <th class="text-warning">Email</th>
        </tr>
      </thead>
      <tbody>
        {% for result in results %}
        <tr>
          <td>{{result.name}}</td>
          <td>{{result.phone}}</td>
          <td>{{result.email}}</td>
          <td><a href="/update_entry?id={{result.id}}"><button class="btn btn-info btn-small" type="button" name="button">Edit Contact</button></a></td>
          <td><a href="/delete_entry?id={{result.id}}"><button class="btn btn-danger btn-small" type="button" name="button">Delete Contact</button></a></td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    <a href="/new_entry"><button class="btn btn-success" type="button" name="button">Add Contact</button></a>
{% endblock %}
```
Each functionality requires two URLs, a route for rendering the HTML page with the corresponding form, and a route for the form action.
```Python
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
```
The forms were both created using the built in form classes in Bootstrap.
```HTML
{% extends 'layout.html' %}

{% block body %}
  <form class="form-horizontal" action="/submit_update_entry" method="post">
    <legend>Update Contact: <span class="text-warning">{{contact.name}}</span></legend>
    <input type="hidden" name="id" value="{{contact.id}}">
    <div class="form-group">
      <label class="control-label text-info" for="name">Name: </label>
      <input class="form-control" type="text" name="name" value="{{contact.name}}">
    </div>
    <div class="form-group">
      <label class="control-label text-info" for="phone">Phone Number: </label>
      <input class="form-control" type="text" name="phone" value="{{contact.phone}}">
    </div>
    <div class="form-group">
      <label class="control-label text-info" for="email">Email: </label>
      <input class="form-control" type="email" name="email" value="{{contact.email}}">
    </div>
    <div class="form-group">
      <button class="btn btn-success" type="submit" name="action" value="save">Save Updated Contact</button>
      <button class="btn btn-danger" type="submit" name="action" value="delete">Delete Contact</button>
    </div>
  </form>
{% endblock %}
```

##Screenshots

![Phonebook1](/img/all_entries.png)
![Phonebook2](/img/create.png)
![Phonebook3](/img/edit_contact.png)
