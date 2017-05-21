import uuid, hashlib

"""
you can get slightly more efficient storage in your database by storing the salt and hashed password as raw bytes
 rather than hex strings. To do so, replace hex with bytes and hexdigest with digest.

 how do you reverse it to get the password back?
    You don't reverse it, you never reverse a password. That's why we hash it and we don't encrypt it.
    If you need to compare an input password with a stored password, you hash the input and compare the hashes.
    If you encrypt a password anyone with the key can decrypt it and see it. It's not safe

    Salts are not considered secret. You store them alongside the username and password hash.
    See here for a fantastic explanation about password hashing in general.
    https://security.stackexchange.com/questions/211/how-to-securely-hash-passwords/31846#31846

"""

password = "test_password"
salt = uuid.uuid4().hex
# For this to work in Python 3 you'll need to UTF-8 encode
hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
print(hashed_password)
