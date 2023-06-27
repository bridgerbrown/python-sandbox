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
