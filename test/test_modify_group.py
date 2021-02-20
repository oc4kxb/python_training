from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name="EditedName"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="EditedHeader"))


def test_modify_group_footer(app):
    app.group.modify_first(Group(footer="EditedFooter"))
