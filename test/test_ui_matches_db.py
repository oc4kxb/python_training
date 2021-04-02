from model.group import Group


def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_groups = map(clean, db.get_group_list())
    ui_groups = app.group.get_groups_list()
    assert sorted(ui_groups, key=Group.id_or_max) == sorted(db_groups, key=Group.id_or_max)
