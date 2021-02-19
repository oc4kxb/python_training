from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="EditedName", footer="EditedFooter"))
    app.session.logout()
