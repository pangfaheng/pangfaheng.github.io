#!/usr/bin/env python3

import random
import string
import sys

# example: python $1 int[password_lenght] int[password_number]

def generate_character():
    characters = string.ascii_letters + string.digits + string.punctuation
    t_characters = ''
    for i in characters:
        if i in 'iIl1o0O':
            continue
        if i not in '!@#$%^&*' and i not in string.ascii_letters and i not in string.digits:
            continue
        t_characters = t_characters + i
    return random.choice(t_characters)

def generate_password(password_lenght):
    password = ''.join(generate_character() for _ in range(password_lenght))
    if check_password_strength(password) is False:
        generate_password(password_lenght)
    return password

def check_password_strength(password):
    remark_letter = False
    remark_digit = False
    remark_punctuation = False
    for i in password:
        if i in string.ascii_letters:
            remark_letter = True
        if i in string.digits:
            remark_digit = True
        if i in string.punctuation:
            remark_punctuation = True
    if remark_letter == True and remark_digit == True and remark_punctuation == True:
        return True
    else:
        return False

def get_password_number():
    password_number = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
    return password_number

def get_password_lenght():
    password_lenght = int(sys.argv[1]) if len(sys.argv) >= 2 else 16
    return password_lenght

if __name__ in '__main__':
    password_number = get_password_number()
    password_lenght = get_password_lenght()
    for i in range(0,password_number):
        generated_password = generate_password(password_lenght)
        print(generated_password)