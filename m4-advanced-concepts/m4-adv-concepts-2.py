#__Benchmarking__

# timeit
def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    import timeit
    setup = "from __main__ import my_function"
    print(timeit.timeit("my_function()", setup=setup))

# timing context manager
import random
import time

class MyTimer():

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))


def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1,5))
        time.sleep(sleep_time)


if __name__ == '__main__':
    with MyTimer():
        long_runner()


#__Encryption and Cryptography__

# Hashes
import hashlib
md5 = hashlib.md5()

md5.update(b'Python rocks!')
print (md5.digest())


import hashlib
sha = hashlib.sha1(b'Hello Python').hexdigest()
print (sha)


# Key Derivation
import hashlib
import binascii
dk = hashlib.pbkdf2_hmac(hash_name='sha256',
        password=b'password@educative', 
        salt=b'educative_salt', 
        iterations=100000)
print (binascii.hexlify(dk))


from Crypto.Protocol.KDF import scrypt

password = b'password@educative'
salt=b'educative_salt'
key = scrypt(password, salt, 16, N=2**14, r=8, p=1)
print(key)

# PyCrypto
from Crypto.Cipher import DES
key = b'abcdefgh'
def pad(text):
        while len(text) % 8 != 0:
            text += b' '
        return text
des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print (encrypted_text)


from Crypto.PublicKey import RSA
code = 'nooneknows'
key = RSA.generate(2048)
print("key: ", key)
encrypted_key = key.exportKey(passphrase=code, pkcs=8, 
        protection="scryptAndAES128-CBC")
with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)
with open('my_rsa_public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())


from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.PublicKey import RSA
code = 'nooneknows'
key = RSA.generate(2048)

encrypted_key = key.exportKey(passphrase=code, pkcs=8, 
        protection="scryptAndAES128-CBC")
with open('my_private_rsa_key.bin', 'wb') as f:
        f.write(encrypted_key)
with open('my_rsa_public.pem', 'wb') as f:
        f.write(key.publickey().exportKey())

with open('encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('my_rsa_public.pem').read())
    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(ciphertext)
    print("data is:")
    print(data)
    print("tag is:")
    print(tag)
    print("ciphertext is:")
    print(ciphertext)

#The Cryptography Package
from cryptography.fernet import Fernet
cipher_key = Fernet.generate_key()
print (cipher_key)


cipher = Fernet(cipher_key)
text = b'My super secret message'
encrypted_text = cipher.encrypt(text)
print (encrypted_text)


decrypted_text = cipher.decrypt(encrypted_text)
print (decrypted_text)


#__Databases__

# SQL
CREATE TABLE table_name (
    id INTEGER,
    name VARCHAR,
    make VARCHAR
    model VARCHAR,
    year DATE,
    PRIMARY KEY (id)
    );

INSERT INTO table_name (id, name, make, model, year) 
VALUES (1, 'Marly', 'Ford', 'Explorer', '2000');

UPDATE table_name
SET name='Chevrolet'
WHERE id=1;

SELECT name, make, model
FROM table_name;

SELECT * FROM table_name;

SELECT name, make, model
FROM table_name
WHERE year >= '2000-01-01' AND 
      year <= '2006-01-01';

DELETE FROM table_name
WHERE name='Ford';

DROP TABLE table_name;


# MySQL
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='educative', password='secret', database='test')
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# get a single row
row = cursor.fetchone()
print('printing the first row:')
print(row)

# disconnect from the database
conn.close()


# PostgreSQL
import psycopg2

string = "postgresql://educative@localhost/test?password=secret"
conn = psycopg2.connect(string)
cursor = conn.cursor()

# execute a query
cursor.execute("SELECT * FROM table_name;")
row = cursor.fetchone() 
print(row)
# close your cursor and connection
cursor.close()
conn.close()


# Object Relational Mappers
import sqlalchemy as sal
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://educative:secret@localhost:5432/test")
conn = engine.connect()
cursor = conn_sql.cursor()
print(engine)
# execute a query
cursor.execute("SELECT * FROM table_name;")
row = cursor.fetchone()
print(row)
# close your cursor and connection
cursor.close()
conn.close()


#__The super built-in__
class MyParentClass():
    def __init__(self, x, y):
        pass

class SubClass(MyParentClass):
    def __init__(self, x, y):
        super().__init__(x, y)

# MRO
class X:
    def __init__(self):
        print('X')
        super().__init__()

class Y:
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)


class Base():
    def __init__(self):
        s = super()
        print(s.__thisclass__)
        print(s.__self_class__)
        s.__init__()

class SubClass(Base):
    pass

sub = SubClass()


#__Descriptors__
class MyDescriptor():
    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value

class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='desc')
    normal = 10

if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)


#__Scope__

# Local Scope
x = 10
def my_func(a, b):
    print(x)
    print(z)


my_func(1, 2)

# Global Scope
def my_func(a, b):
    global x
    print(x)
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)

# nonLocal Scope
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer
c = counter()

print (c)
print (c())
print (c())
print (c())


#__Web Scraping__
import requests
from bs4 import BeautifulSoup

url = 'https://www.educative.io/blog/get-started-with-python-debuggers'

def get_articles():
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.findAll('h1')

    articles = {i.a['href']: i.text.strip()
                for i in pages if i.a}
    
    for article in articles:
        s = '{title}: {url}'.format(title=articles[article].encode('utf-8'),url=article)
        print(s)

    return articles

if __name__ == '__main__':
    articles = get_articles()


#__Working with FTP__
from ftplib import FTP
ftp = FTP('ftp.cse.buffalo.edu')
print (ftp.login())
#'230 Guest login ok, access restrictions apply.'

from ftplib import FTP
ftp = FTP()
HOST = 'ftp.cse.buffalo.edu'
PORT = 12345
ftp.connect(HOST, PORT)


from ftplib import FTP
ftp = FTP('ftp.cse.buffalo.edu')
ftp.login()

print(ftp.retrlines('LIST'))
#drwxr-xr-x    2 202019   5564         4096 Feb 10 11:34 CSE421
#drwxr-xr-x    2 202019   5564         4096 Feb 10 11:35 CSE468
#drwx------    2 0        0           16384 Sep 17  2020 lost+found
#drwxr-xr-x    6 89987    329651       4096 Sep 05  2015 mirror
#drwxrwxr-x    4 6980     546          4096 Sep 23  2020 pub
#drwxr-xr-x   14 0        120          4096 Sep 23  2020 users
#226 Directory send OK.

print(ftp.cwd('mirror'))
#250 Directory successfully changed.


from ftplib import FTP

ftp = FTP('ftp.debian.org')
print(ftp.login())
#'230 Login successful.'

print(ftp.cwd('debian')  )
#'250 Directory successfully changed.'


out = 'README'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'README.html', f.write)

#__The urllib Module__
import urllib.request
url = urllib.request.urlopen('https://www.google.com/')
print (url.geturl())
#'https://www.google.com/'
print (url.info())
#<http.client.HTTPMessage object at 0x7fddc2de04e0>
header = url.info()
print (header.as_string())
print (url.getcode())
#200

import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
response = urllib.request.urlopen(url)
data = response.read()
with open('test.zip', 'wb') as fobj:
    fobj.write(data)

from urllib.parse import urlparse
result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print (result)
print (result.netloc)
print (result.geturl())
print (result.port)

import urllib.robotparser
robot = urllib.robotparser.RobotFileParser()
print (robot.set_url('http://arstechnica.com/robots.txt'))
#None
print (robot.read())
#None
print (robot.can_fetch('*', 'http://arstechnica.com/'))
#True
print (robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))
#False


#__The unittest Module__
import mymath
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


if __name__ == '__main__':
    unittest.main()


#__The mock Module__
from unittest.mock import Mock
my_mock = Mock()
my_mock.__str__ = Mock(return_value='Mocking')
print(str(my_mock))
#'Mocking'


#__The asyncio Module__
import asyncio

async def my_coro():
    await func()


import asyncio
import functools


def event_handler(loop, stop=False):
    print('Event handler called')
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(functools.partial(event_handler, loop))
        print('starting event loop')
        loop.call_soon(functools.partial(event_handler, loop, stop=True))

        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close() 


#__The threading Module__
import threading


def doubler(number):
    """
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()


if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()



import threading

total = 0
lock = threading.Lock()

def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()
    print (total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()


import threading

total = 0
lock = threading.Lock()

def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    with lock:
        total += amount
    print (total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()


#__The multiprocessing Module__
import os

from multiprocessing import Process


def doubler(number):
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


#__The concurrent.futures Module__
import os
import urllib.request

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def downloader(url):
    """
    Downloads the specified URL and saves it to disk
    """
    req = urllib.request.urlopen(url)
    filename = os.path.basename(url)
    ext = os.path.splitext(url)[1]
    if not ext:
        raise RuntimeError('URL does not contain an extension')

    with open(filename, 'wb') as file_handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg


def main(urls):
    """
    Create a thread pool and download specified urls
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(downloader, url) for url in urls]
        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    main(urls)
