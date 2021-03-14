from random import randrange

from model.contact import Contact


def test_modify_some_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="modify", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="EditedLastName")
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_by_index(contact, index)
    assert app.contact.count() == len(old_contacts)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
