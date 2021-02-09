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
        # open home page
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # open contact creation page
        wd.find_element_by_link_text("add new").click()
        # fill names
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Evgeni")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Valerevich")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Bayrambekov")
        # fill nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("oc4kxb")
        # upload photo
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        photo_path = os.path.join(current_dir, 'fitness-gym-logo-premium-vector_144543-140.jpg')
        wd.find_element_by_name("photo").send_keys(photo_path)
        # fill company name
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("MyCompany")
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("QA")
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("region, city, street, building, flat")
        # fill home phone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("44620")
        # fill mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("9992002020")
        # fill work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("9990020202")
        # fill email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("dadada@email.mail")
        # fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("mysite.com/oc4kxb")
        # fill birthdate
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("24")
        wd.find_element_by_xpath("//option[@value='24']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("December")
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1993")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()
    
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
