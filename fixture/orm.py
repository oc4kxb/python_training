from datetime import datetime
from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact,
                       table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        secondary_phone = Optional(str, column='phone2')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup,
                     table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, database, user, password):
        self.db.bind(provider='mysql', host=host, database=database, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, orm_groups):
        def convert(orm_group):
            return Group(id=str(orm_group.id), name=orm_group.name, header=orm_group.header, footer=orm_group.footer)
        return list(map(convert, orm_groups))

    @db_session
    def get_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, orm_contacts):
        def convert(orm_contact):
            return Contact(id=str(orm_contact.id), firstname=orm_contact.firstname, lastname=orm_contact.lastname,
                           address=orm_contact.address, home_phone=orm_contact.home_phone,
                           mobile_phone=orm_contact.mobile_phone, work_phone=orm_contact.work_phone,
                           secondary_phone=orm_contact.secondary_phone, email=orm_contact.email,
                           email2=orm_contact.email2, email3=orm_contact.email3)
        return list(map(convert, orm_contacts))

    @db_session
    def get_contacts_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
