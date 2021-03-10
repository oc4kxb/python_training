from model.contact import Contact


def test_modify_contact_lastname(app):
    if len(app.contact.get_contacts_list()) == 0:
        app.contact.create(Contact(lastname="modify", firstname="test"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(lastname="EditedLastName")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[0] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
