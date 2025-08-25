import random

def game(pass_length):
    elements = "1", "2", "3"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    