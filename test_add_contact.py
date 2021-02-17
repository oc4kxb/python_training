# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="Evgeni", middlename="Valerevich", lastname="Bayrambekov", nickname="oc4kxb", company_name="MyCompany", employee_title="QA",
                        address="region, city, street, building, flat", home_phone="44620", mobile_phone="9992002020", work_phone="9990020202",
                        email="dadada@email.mail", homepage="mysite.com/oc4kxb", birth_day="24", birth_month="December", birth_year="1993",
                        photo_name="fitness-gym-logo-premium-vector_144543-140.jpg"))
    app.logout()
