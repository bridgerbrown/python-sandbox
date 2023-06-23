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


#__Context Managers__
with open(path, 'w') as f_obj:
    f_obj.write(some_data)


from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print("Closing file")
        f_obj.close()

if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')

# Contextlib and its classes
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("http://www.google.com")) as webpage:
    for line in webpage:
        # process the line
        pass


from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)


from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)

# ExitStack and Reentrant Context Managers
from contextlib import ExitStack

filenames = []
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename))
        for filename in filenames]


# __The functools module__

# lru_cache
import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Gets the specified Python module web page
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


if __name__ == "__main__":
    modules = ["functools", "collections", "os", "sys"]
    for module in modules:
        page = get_webpage(module)
    if page:
        print("{} module page found".format(module))

# functool.partial
from functools import partial

def add(x, y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))

# functool.singledispatch
from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])

# functools.wraps
from functools import wraps

def another_function(func):
    """
    A function that accepts another function
    """

    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    #a_function()
    print(a_function.__name__)
    print(a_function.__doc__)


#__All About Imports__

# Regular imports
import sys
import os, sys, time
import sys as system # Renaming
import urllib.error # Certain submodules import with dot notation

# Using from
from functools import lru_cache
functools.lru_cache(*args) # The normal way

from os import path, walk, unlink
from os import (path, walk, 
                remove, rename)
from os import path, walk, unlink, \
                remove, rename

# Relative imports
from . module_y import spam as ham

import sys
sys.path.append('/usercode/my_package')
import my_package



