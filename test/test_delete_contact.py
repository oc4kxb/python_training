from random import randrange

from model.contact import Contact


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="delete", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert app.contact.count() == len(old_contacts) - 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts
