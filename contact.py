import os

class Contact:
    def __init__(self, firstname = "", middlename = "", nickname = "", lastname = "", company_name = "", employee_title = "", address = "",
                       home_phone = "", mobile_phone = "", work_phone = "", email = "", homepage = "", birth_day = "", birth_month = "", birth_year = "", photo_name = ""):
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

    def get_photo_path(self, photo_name):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(current_dir, photo_name)
