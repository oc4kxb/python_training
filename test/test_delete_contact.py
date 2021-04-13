import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui, data_contacts):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(data_contacts)
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    old_contacts.remove(contact)
    assert new_contacts == old_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_remove_contact_from_group(app, db, data_contacts, data_groups):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(data_contacts)
    if len(db.get_groups_list()) == 0:
        app.group.create(data_groups)
    group = random.choice(db.get_groups_list())
    contact = random.choice(db.get_contacts_list())
    old_contacts_in_group = db.get_contacts_list_in_group(group)
    if len(old_contacts_in_group) == 0:
        app.contact.add_in_group(contact, group)
        old_contacts_in_group = db.get_contacts_list_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.remove_from_group(contact, group)
    new_contacts_in_group = db.get_contacts_list_in_group(group)
    old_contacts_in_group.remove(contact)
    assert new_contacts_in_group == old_contacts_in_group
