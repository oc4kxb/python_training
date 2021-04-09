import random
from model.group import Group


def test_delete_some_group(app, db, check_ui, data_groups):
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_groups_list()
    assert len(new_groups) == len(old_groups) - 1
    old_groups.remove(group)
    assert new_groups == old_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
