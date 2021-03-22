def test_contact_info(app):
    contact_on_home_page = app.contact.get_contacts_list()[0]
    contact_on_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_on_home_page == contact_on_edit_page # id, firstname, lastname
    assert contact_on_home_page.address == contact_on_edit_page.address
    assert contact_on_home_page.all_emails_from_home_page == contact_on_edit_page.all_emails_from_home_page
    assert contact_on_home_page.all_phones_from_home_page == contact_on_edit_page.all_phones_from_home_page
