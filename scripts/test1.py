import random


def dood_password_generator(length):
    alphabet = ('0123456789'
                'abcdefghijklmnopqrstuvwxyz'
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                '!@#$%^&*()_+')
    result = ''
    for i in range(10):
        symb = random.choice(alphabet)
        result += symb

    return result


print(dood_password_generator(10))

with open('../pop_pas.txt') as f:
    content = f.read()

passwords = content.split("\n")

i = 0


def bad_pas_gen():
    global i
    password = passwords[i]
    i += 1
    return password


print(bad_pas_gen())
print(bad_pas_gen())
print(bad_pas_gen())
print(bad_pas_gen())
