import random

def gen_word(pass_length):
    elements = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    