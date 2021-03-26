import json
import random
import string
import os.path
from model.group import Group


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + 10*" "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


empty_and_some_random = [Group(name="", header="", footer="")] + [
    Group(name=random_string('name', 10), header=random_string('header', 20), footer=random_string('footer', 20))
    for i in range(5)
]

all_variants_with_empty = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string('name', 10)]
    for header in ["", random_string('header', 20)]
    for footer in ["", random_string('footer', 20)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(empty_and_some_random, default=lambda x: x.__dict__, indent=2))
