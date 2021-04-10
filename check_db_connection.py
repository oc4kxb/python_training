from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")

try:
    list = db.get_contacts_in_group(Group(id=6))
    for element in list:
        print(element)
    print(len(list))
finally:
    pass
