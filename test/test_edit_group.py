from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="EditedName", header="EditedHeader", footer="EditedFooter"))
    app.session.logout()
