# __Intro to Argument Parsing using argparse__
import argparse

parser = argparse.ArgumentParser(
    description="A simple argument parser",
    epilog="This is example usage",
)

parser.print_help()

# __The collections module__

# ChainMap
from collections import ChainMap

car_parts = {"hood": 500, "engine": 5000, "front_door": 750}
car_options = {"A/C": 1000, "Turbo": 2500, "rollbar": 300}
car_accessories = {"cover": 100, "hood_ornament": 150, "seat_cover": 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print(car_pricing["hood"])


import argparse
import os

from collections import ChainMap

def main():
    app_defaults = {"username": "admin", "password": "admin"}

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}

    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain["username"])


if __name__ == "__main__":
    main()
    os.environ["username"] = "test"
    main()


# Counter
from collections import Counter

print(Counter("Blahblah"))

counter = Counter("Blahblah")
print(counter["u"])

print(list(counter.elements()))

print(counter.most_common(2))

counter_one = Counter("superfluous")
print(counter_one)

counter_two = Counter("super")
print(counter_one.subtract(counter_two))
print(counter_one)


# defaultdict
from collections import defaultdict

sentance = "The redfor over the zoo the food."
words = sentance.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)


animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'

print(animal['Nick'])
print(animal)


# deque
from collections import deque
import string

d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)

d.appendleft("test")

d.rotate(1)
print(d)

# namedTuple
from collections import namedtuple

Parts = namedtuple("Parts", "id_num desc cost amount")
auto_parts = Parts(id_num="1234", desc="Ford Engine", cost=1200.00, amount=10)
print(auto_parts.id_num)


Parts = {'id_num':'1234', 'desc':'Ford Engine',
     'cost':1200.00, 'amount':10}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print (parts)


# OrderedDict
from collections import OrderedDict

d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
new_d = OrderedDict(sorted(d.items()))
print(new_d)


for key in new_d:
    print(key, new_d[key])
