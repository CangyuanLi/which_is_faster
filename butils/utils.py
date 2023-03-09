import random
import string

def generate_ascii(min_len: int=1, max_len: int=20):
    length = random.randint(min_len, max_len)

    return "".join(random.choices(string.printable, k=length))

def generate_ascii_list(min_len, max_len, list_len):
    return [generate_ascii() for _ in range(list_len)]

def generate_int(min: int=-100, max: int= 100):
    return random.randint(min, max)

def generate_float(min: int=-100, max: int=100):
    return random.uniform(min, max)