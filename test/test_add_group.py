# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="dsadas", header="dasdasdasd", footer="dsadsad")
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

