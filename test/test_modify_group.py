from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify_name_test"))
    app.group.modify_first(Group(name="EditedName"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify_header_test"))
    app.group.modify_first(Group(header="EditedHeader"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify_footer_test"))
    app.group.modify_first(Group(footer="EditedFooter"))
