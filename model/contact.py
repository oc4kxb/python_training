import os
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, nickname=None, lastname=None, company_name=None,
                 employee_title=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 secondary_phone=None, email=None, email2=None, email3=None, homepage=None, birth_day=None,
                 birth_month=None, birth_year=None, photo_name=None, id=None, all_phones=None,
                 all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company_name = company_name
        self. employee_title = employee_title
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.photo_name = photo_name
        self.id = id
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname.strip() == other.firstname.strip() and self.lastname.strip() == other.lastname.strip()

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    @staticmethod
    def get_photo_path(photo_name):
        return os.path.join(os.getcwd() + "\\..\\files", photo_name)
