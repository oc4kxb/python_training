import re


def test_contact_info(app):
    contact_on_home_page = app.contact.get_contacts_list()[0]
    contact_on_edit_page = app.contact.get_contact_info_from_edit_page(0)
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
