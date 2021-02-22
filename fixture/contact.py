from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # click edit first contact button
        wd.find_element_by_xpath("//tr[@name='entry']//img[@title='Edit']").click()
        self.fill_form(new_contact_data)
        # click update button
        wd.find_element_by_css_selector("[value='Update']").click()
        # return to home page
        self.app.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_css_selector("[value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        # return to home page
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_form(self, contact):
        wd = self.app.wd
        # fill names
        self.change_text_field_value("firstname", contact.firstname)
        self.change_text_field_value("middlename", contact.middlename)
        self.change_text_field_value("lastname", contact.lastname)
        # fill nickname
        self.change_text_field_value("nickname", contact.nickname)
        # upload photo
        self.upload_photo("photo", contact.photo_name)
        # fill company name
        self.change_text_field_value("company", contact.company_name)
        # fill title
        self.change_text_field_value("title", contact.employee_title)
        # fill address
        self.change_text_field_value("address", contact.address)
        # fill home phone
        self.change_text_field_value("home", contact.home_phone)
        # fill mobile phone
        self.change_text_field_value("mobile", contact.mobile_phone)
        # fill work phone
        self.change_text_field_value("work", contact.work_phone)
        # fill email
        self.change_text_field_value("email", contact.email)
        # fill homepage
        self.change_text_field_value("homepage", contact.homepage)
        # fill birthdate
        self.change_select_field_value("bday", contact.birth_day)
        self.change_select_field_value("bmonth", contact.birth_month)
        self.change_text_field_value("byear", contact.birth_year)

    def change_text_field_value(self, element_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(element_name).click()
            wd.find_element_by_name(element_name).clear()
            wd.find_element_by_name(element_name).send_keys(text)

    def change_select_field_value(self, element_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(element_name).click()
            Select(wd.find_element_by_name(element_name)).select_by_visible_text(value)
            wd.find_element_by_xpath("//option[@value='" + value + "']").click()

    def upload_photo(self, element_name, file_name):
        wd = self.app.wd
        if file_name is not None:
            photo_path = Contact.get_photo_path(file_name)
            wd.find_element_by_name("photo").send_keys(photo_path)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))
