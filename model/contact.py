import os


class Contact:

    def __init__(self, firstname=None, middlename=None, nickname=None, lastname=None, company_name=None,
                 employee_title=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 email=None, homepage=None, birth_day=None, birth_month=None, birth_year=None,
                 photo_name=None, id=None):
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
        self.email = email
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.photo_name = photo_name
        self.id = id

    def __repr__(self):
        return "%s:%s-%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname and self.lastname == other.lastname

    @staticmethod
    def get_photo_path(photo_name):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_dir, photo_name)
