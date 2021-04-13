import random
from model.contact import Contact


def test_modify_some_contact_lastname(app, db, check_ui, data_contacts):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(data_contacts)
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    contact.lastname = "EditedLastName"
    app.contact.modify(contact)
    new_contacts = db.get_contacts_list()
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
