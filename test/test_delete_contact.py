import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui, data_contacts):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(data_contacts)
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert new_contacts == old_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
