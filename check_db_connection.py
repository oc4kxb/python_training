from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", database="addressbook", user="root", password="")

try:
    list = db.get_group_list()
    for element in list:
        print(element)
    print(len(list))
finally:
    pass
