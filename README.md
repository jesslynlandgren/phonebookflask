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

```Python
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
```

##Screenshots

![Phonebook1](/img/all_entries.png)
![Phonebook2](/img/create.png)
![Phonebook3](/img/edit_contact.png)
