from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
import re

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_contact_creation_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creation_page()
        self.fill_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_first(self, new_contact_data):
        self.modify_by_index(new_contact_data, 0)

    def modify_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_form(new_contact_data)
        # click update button
        wd.find_element_by_css_selector("[value='Update']").click()
        # return to home page
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_by_index(index)
        # click delete button
        wd.find_element_by_css_selector("[value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        # wait delete confirmation message
        WebDriverWait(wd, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        # return to home page
        self.open_contacts_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") or wd.current_url.endswith("addressbook/index.php")):
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
        try:
            self.upload_photo("photo", contact.photo_name)
        except InvalidArgumentException:
            pass
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

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        edit_buttons = wd.find_elements_by_xpath("//tr[@name='entry']//a[img[@title='Edit']]")
        edit_buttons[index].click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        view_buttons = wd.find_elements_by_xpath("//tr[@name='entry']//a[img[@title='Details']]")
        view_buttons[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, secondary_phone=secondary_phone,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone)
