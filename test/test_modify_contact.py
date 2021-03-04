from model.contact import Contact


def test_modify_contact_lastname(app):
    if len(app.contact.get_contacts_list()) == 0:
        app.contact.create(Contact(lastname="modify", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.modify_first(Contact(lastname="EditedLastName"))
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts)
