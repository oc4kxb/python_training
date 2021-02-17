# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import Contact
from application import Application
import unittest


class TestAddContact(unittest.TestCase):

    def setUp(self):
        self.app = Application()
    
    def test_add_contact(self):
        self.app.login("admin", "secret")
        self.app.create_contact(Contact(firstname="Evgeni", middlename="Valerevich", lastname="Bayrambekov", nickname="oc4kxb", company_name="MyCompany", employee_title="QA",
                            address="region, city, street, building, flat", home_phone="44620", mobile_phone="9992002020", work_phone="9990020202",
                            email="dadada@email.mail", homepage="mysite.com/oc4kxb", birth_day="24", birth_month="December", birth_year="1993",
                            photo_name="fitness-gym-logo-premium-vector_144543-140.jpg"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
