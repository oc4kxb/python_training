# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname="Errr", middlename="Vrrr", lastname="Brrr", nickname="oc4kxb", company_name="MyCompany", employee_title="QA",
                               address="region, city, street, building, flat", home_phone="44620", mobile_phone="9992002020", work_phone="9990020202",
                               email="dadada@email.mail", homepage="mysite.com/oc4kxb", birth_day="14", birth_month="December", birth_year="1993",
                               photo_name="avatar.jpg"))
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts) + 1

