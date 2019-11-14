import hashlib
import pickle


def hash256(*args):
    data = bytes()
    for arg in args:
        data += pickle.dumps(args)
    return hashlib.sha256(data).hexdigest()


def __random(length):
    from random import random

    value = random()
    return hash256(value)[:length]


def get_rand_value(length):
    """256 characters maximum."""
    if length > 256:
        length = 256
    try:
        with open("/dev/urandom", "rb") as fd:
            return (fd.read(length // 2 + 1)).hex()[:length]
    except Exception:
        return __random(length)
