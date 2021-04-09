from fixture.db import DbFixture

db = DbFixture(host="localhost", database="addressbook", user="root", password="")

try:
    contacts = db.get_contacts_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
