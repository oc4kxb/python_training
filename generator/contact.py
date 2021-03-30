import getopt
import sys
import random
import string
import os.path
import jsonpickle
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

count = 2
file = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        count = int(a)
    elif o == "-f":
        file = a


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


test_data = [Contact(
            firstname=random_string("firstname", 15),
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
    for i in range(count)
]

f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(f, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
