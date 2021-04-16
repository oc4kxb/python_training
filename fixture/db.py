from fixture.orm import ORMFixture


class DbFixture:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.orm = ORMFixture(host=host, database=database, user=user, password=password)

    def get_groups_list(self):
        return self.orm.get_groups_list()

    def get_contacts_list(self):
        return self.orm.get_contacts_list()

    def get_contacts_list_in_group(self, group):
        return self.orm.get_contacts_in_group(group)

    def get_contacts_not_in_group(self, group):
        return self.orm.get_contacts_not_in_group(group)
