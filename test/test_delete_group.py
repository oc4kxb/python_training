from random import randrange

from model.group import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="delete_test"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert app.group.count() == len(old_groups) - 1
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert new_groups == old_groups
