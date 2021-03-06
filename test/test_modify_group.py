import random
from model.group import Group


def test_modify_group_name(app, db, check_ui, data_groups):
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    group.name = "EditedName"
    app.group.modify(group)
    new_groups = db.get_groups_list()
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui, data_groups):
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    group.header = "EditedHeader"
    app.group.modify(group)
    new_groups = db.get_groups_list()
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui, data_groups):
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    group.footer = "EditedFooter"
    app.group.modify(group)
    new_groups = db.get_groups_list()
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
