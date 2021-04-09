from datetime import datetime
from pony.orm import *
from model.group import Group


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, database, user, password):
        self.db.bind(provider='mysql', host=host, database=database, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, orm_groups):
        def convert(orm_group):
            return Group(id=str(orm_group.id), name=orm_group.name, header=orm_group.header, footer=orm_group.footer)
        return list(map(convert, orm_groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
