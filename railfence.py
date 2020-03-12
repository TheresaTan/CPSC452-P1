# Julian Coronado
# 03/10/20

import math
import numpy as np

# gets usr input
usr_input = input("Enter a string: ")
# sets all to lowercase and removes white space
plaintext = usr_input.replace(" ", "").lower()
# gets usr key size input
key = int(input("Enter a key size: "))

# print("Plaintext:", plaintext)
# print("Plaintext Length:", len(plaintext))
# print("Key Size:", key, "\n")

n = len(plaintext)

m = math.floor(n / key)

if n % key > 0:
    m += 1

# generate matrix using numpy
railfenceMatrix = np.chararray((key, m))

# temp - assigns all indices to "-"
railfenceMatrix[:] = '-'

# temp - displays matrix
print(railfenceMatrix)
