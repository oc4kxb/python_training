from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="delete", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts) - 1
    old_contacts[0:1] = []
    assert new_contacts == old_contacts
