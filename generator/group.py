import getopt
import sys
import random
import string
import os.path
import jsonpickle
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

count = 5
file = "data/groups.json"

for o, a in opts:
    if o == "-n":
        count = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + 10*" "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(
    name=random_string('name', 10),
    header=random_string('header', 20),
    footer=random_string('footer', 20))
    for i in range(count)
]

f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(f, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
