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
    contact = random.choice(db.get_contacts_list())
    group = random.choice(db.get_groups_list())
    old_contacts_in_group = db.get_contacts_list_in_group(group)
    app.contact.add_in_group(contact, group)
    new_contacts_in_group = db.get_contacts_list_in_group(group)
    if contact not in old_contacts_in_group:
        old_contacts_in_group.append(contact)
    assert sorted(new_contacts_in_group, key=Contact.id_or_max) == \
           sorted(old_contacts_in_group, key=Contact.id_or_max)
