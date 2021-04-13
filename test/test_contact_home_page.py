import re
from random import randrange


def test_contact_info(app, db):
    contacts_on_home_page = app.contact.get_contacts_list()
    contacts_on_db = db.get_contacts_list()
    assert contact_on_home_page == contact_on_edit_page  # id, firstname, lastname
    assert contact_on_home_page.address == contact_on_edit_page.address
    assert contact_on_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_on_edit_page)
    assert contact_on_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_on_edit_page)


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
