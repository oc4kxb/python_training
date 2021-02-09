# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import os


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_contact_creation_page(wd)
        self.create_contact(wd, "Evgeni", "Valerevich", "oc4kxb", "Bayrambekov", "MyCompany", "QA",
                            "region, city, street, building, flat", "44620", "9992002020", "9990020202",
                            "dadada@email.mail", "mysite.com/oc4kxb", "24", "December", "1993")
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, firstname, middlename, nickname, lastname, company_name, employee_title, address,
                       home_phone, mobile_phone, work_phone, email, homepage, birth_day, birth_month, birth_year):
        # fill names
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        # fill nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        # upload photo
        current_dir = os.path.abspath(os.path.dirname(__file__))
        photo_path = os.path.join(current_dir, 'fitness-gym-logo-premium-vector_144543-140.jpg')
        wd.find_element_by_name("photo").send_keys(photo_path)
        # fill company name
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company_name)
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(employee_title)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        # fill home phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        # fill mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile_phone)
        # fill work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(work_phone)
        # fill email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        # fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(homepage)
        # fill birthdate
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(birth_day)
        wd.find_element_by_xpath("//option[@value='24']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(birth_month)
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birth_year)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_creation_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
