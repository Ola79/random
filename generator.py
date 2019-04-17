"""
generator imion
"""
from random import choice, choices, randint, sample


lista_liter = "abcdefghijklmnopqrstuvwxz"


def generate_letter_list(l_l):
    characters = [char for char in l_l]
    print(characters)


generate_letter_list(lista_liter)

print(choice(lista_liter))

name = ''.join(sample(lista_liter, 6))

print(name)


# white = "".join(["_" if _ % 2 != 0 else "#" for _ in range(size)])
# black = "".join(["#" if _ % 2 != 0 else "_" for _ in range(size)])
# print("\n".join([white if _ % 2 != 0 else black for _ in range(size)]))




