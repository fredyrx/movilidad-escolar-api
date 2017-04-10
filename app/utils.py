import hashlib
import string 
import random

def generate_random_string(length=64):
	characters = string.letters + string.digits
	return "".join([random.choice(characters) for _ in xrange(length)])


def generate_hash(string_base):
	return hashlib.sha256(string_base).hexdigest()