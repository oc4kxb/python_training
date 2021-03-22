# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + 10*" "
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
    for i in range(5)
]


# test_data = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string('name', 10)]
#     for header in ["", random_string('header', 20)]
#     for footer in ["", random_string('footer', 20)]
# ]


@pytest.mark.parametrize("group", test_data, ids=[str(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

