from model.contact import Contact


def test_modify_contact_lastname(app):
    app.contact.modify_first(Contact(lastname="EditedLastName"))
