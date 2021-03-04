from model.contact import Contact


def test_delete_contact(app):
    if len(app.contact.get_contacts_list()) == 0:
        app.contact.create(Contact(lastname="delete", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts) - 1
