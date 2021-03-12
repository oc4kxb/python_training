from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modify_name_test"))
    old_groups = app.group.get_groups_list()
    group = Group(name="EditedName")
    group.id = old_groups[0].id
    app.group.modify_first(group)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if len(app.group.get_groups_list()) == 0:
        app.group.create(Group(name="modify_header_test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(header="EditedHeader"))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)


def test_modify_group_footer(app):
    if len(app.group.get_groups_list()) == 0:
        app.group.create(Group(name="modify_footer_test"))
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(footer="EditedFooter"))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)
