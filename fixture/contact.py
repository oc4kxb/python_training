from selenium.webdriver.support.select import Select


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

    def edit_first(self, contact):
        wd = self.app.wd
        # click home link
        wd.find_element_by_link_text("home").click()
        # click edit first contact button
        wd.find_element_by_xpath("//tr[@name='entry']//img[@title='Edit']").click()
        self.fill_form(contact)
        # click update button
        wd.find_element_by_css_selector("[value='Update']").click()
        # return to home page
        self.app.return_to_home_page()

    def fill_form(self, contact):
        wd = self.app.wd
        # fill names
        if contact.firstname != "":
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(contact.firstname)
        if contact.middlename != "":
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(contact.middlename)
        if contact.lastname != "":
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(contact.lastname)
        if contact.nickname != "":
            # fill nickname
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(contact.nickname)
        if contact.photo_name != "":
            # upload photo
            photo_path = contact.get_photo_path(contact.photo_name)
            wd.find_element_by_name("photo").send_keys(photo_path)
        if contact.company_name != "":
            # fill company name
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(contact.company_name)
        if contact.employee_title != "":
            # fill title
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(contact.employee_title)
        if contact.address != "":
            # fill address
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(contact.address)
        if contact.home_phone != "":
            # fill home phone
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(contact.home_phone)
        if contact.mobile_phone != "":
            # fill mobile phone
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        if contact.work_phone != "":
            # fill work phone
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(contact.work_phone)
        if contact.email != "":
            # fill email
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(contact.email)
        if contact.homepage != "":
            # fill homepage
            wd.find_element_by_name("homepage").clear()
            wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if contact.birth_day != "":
            # fill birthdate
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
            wd.find_element_by_xpath("//option[@value='24']").click()
        if contact.birth_month != "":
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
            wd.find_element_by_xpath("//option[@value='December']").click()
        if contact.birth_year != "":
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.birth_year)

    def delete_first(self):
        wd = self.app.wd
        # click home link
        wd.find_element_by_link_text("home").click()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # click delete button
        wd.find_element_by_css_selector("[value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to home page
        wd.find_element_by_link_text("home").click()
