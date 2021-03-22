# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = random.choice([string.ascii_letters + string.digits])
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


def random_phone(prefix):
    return prefix + "+7" + "".join([random.choice(string.digits) for i in range(10)])


def random_email(prefix):
    letter_string = "".join([random.choice(string.ascii_letters) for i in range(5, 10)])
    domain_after_dot = "".join([random.choice(string.ascii_letters) for i in range(2, 4)])
    return prefix + letter_string + "@" + letter_string + "." + domain_after_dot


def random_site(prefix):
    some_name = "".join([random.choice(string.ascii_letters + string.digits) for i in range(5, 15)])
    some_domain = "".join([random.choice(string.ascii_letters) for i in range(2, 4)])
    return prefix + "www." + some_name + "." + some_domain


def random_day():
    return str(random.choice(range(1, 29)))


def random_month():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    return random.choice(months)


def random_year(prefix):
    return prefix + str(random.choice(range(1920, 2021)))


test_data = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 15),
            middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 15),
            nickname=random_string("nickname", 7),
            company_name=random_string("company", 10),
            employee_title=random_string("title", 10),
            address=random_string("address", 50),
            home_phone=random_phone("home"),
            mobile_phone=random_phone("mobile"),
            work_phone=random_phone("work"),
            email=random_email("email"),
            homepage=random_site("website"),
            birth_day=random_day(),
            birth_month=random_month(),
            birth_year=random_year("year"),
            photo_name="avatar.jpg")
]


@pytest.mark.parametrize("contact", test_data, ids=[str(contact) for contact in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
