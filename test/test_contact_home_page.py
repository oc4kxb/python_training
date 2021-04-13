import re
from model.contact import Contact


def test_contact_info(app, db):
    contacts_on_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contacts_on_db = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    for c in contacts_on_db:
        c.all_phones = merge_phones_like_home_page(c)
        c.all_emails = merge_emails_like_home_page(c)
    assert contacts_on_home_page == contacts_on_db  # id, firstname, lastname, address, phones, emails


def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "", [contact.email, contact.email2, contact.email3]))


def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def clear(s):
    return re.sub("[() -]", "", s)
