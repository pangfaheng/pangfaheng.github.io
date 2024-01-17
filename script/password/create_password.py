#!/usr/bin/env python3

# use:
#   python $0 int[password_lenght] int[password_number]
#
# example: 
#   ./create_password.py 16 1

import random
import string
import sys

def generate_character():
    characters = ''
    for i in string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation:
        if i in 'iIl1o0O':
            continue
        if i not in '!@$%^&*' and i not in string.ascii_lowercase + string.ascii_uppercase + string.digits:
            continue
        characters = characters + i
    return random.choice(characters)

def generate_password(password_lenght, lop_num=0):
    password = ''.join(generate_character() for _ in range(password_lenght))
    if check_password_strength(password) is False and lop_num < 10:
        lop_num += 1
        password = generate_password(password_lenght, lop_num)
    elif check_password_strength(password) is False and lop_num == 10:
        return '---------- try again -----------'
    return password

def check_password_strength(password):
    remark_lowercase = False
    remark_luppercase = False
    remark_digit = False
    remark_punctuation = False
    for i in password:
        if i in string.ascii_lowercase:
            remark_lowercase = True
        if i in string.ascii_uppercase:
            remark_luppercase = True
        if i in string.digits:
            remark_digit = True
        if i in string.punctuation:
            remark_punctuation = True
    if remark_lowercase == True and remark_luppercase == True and remark_digit == True and remark_punctuation == True:
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
        generated_password = generate_password(password_lenght, 0)
        print(generated_password)