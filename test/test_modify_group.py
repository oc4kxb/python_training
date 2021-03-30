from random import randrange

from model.group import Group


def test_modify_group_name(app, data_groups):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group = Group(name="EditedName")
    group.id = old_groups[index].id
    app.group.modify_by_index(group, index)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[index] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_modify_group_header(app, data_groups):
    if len(app.group.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(header="EditedHeader"))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)


def test_modify_group_footer(app, data_groups):
    if len(app.group.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = app.group.get_groups_list()
    app.group.modify_first(Group(footer="EditedFooter"))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)
