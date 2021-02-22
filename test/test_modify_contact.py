from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="modify", firstname="test"))
    app.contact.modify_first(Contact(lastname="EditedLastName"))
