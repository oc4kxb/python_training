import random
from model.contact import Contact


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contacts_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_add_contact_in_group(app, db, data_contacts, data_groups):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(data_contacts)
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    contacts_not_in_group = []
    for g in db.get_groups_list():
        for c in db.get_contacts_not_in_group(g):
            contacts_not_in_group.append(c)
    if len(contacts_not_in_group) == 0:
        app.contact.create(data_contacts)
        contacts_not_in_group.append(db.get_contacts_not_in_group(g)[0])
    contact = random.choice(contacts_not_in_group)
    group = random.choice(db.get_groups_list())
    old_contacts_in_group = db.get_contacts_list_in_group(group)
    app.contact.add_in_group(contact, group)
    new_contacts_in_group = db.get_contacts_list_in_group(group)
    old_contacts_in_group.append(contact)
    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == \
           sorted(old_contacts_in_group, key=Contact.id_or_max)
