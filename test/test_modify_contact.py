from model.contact import Contact


def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact(lastname="EditedLastName"))
    app.session.logout()
