# Julian Coronado
# 03/10/20

import math

# gets usr input
usr_input = input("Enter a string: ")
# sets all to lowercase and removes white space
plaintext = usr_input.replace(" ", "").lower()
# gets usr key size input
key = int(input("Enter a key size: "))

print("Plaintext:", plaintext)
print("Plaintext Length:", len(plaintext))
print("Key Size:", key, "\n")

n = len(plaintext)
# this is what is wrong (i'm pretty sure)
m = (n % key) + 1
# print to display m
# print("m:", m, "\n")

# generate matrix (m here gives the errors sometimes)
rail = [["-"] * m] * key

for i in range(0, m):
    for j in range(0, key):
        # test adding zeros to the matrix
        # needs to fit all characters, vertically then horizontally
        # running into problems with the matrix size
        rail[i][j] = "0"

for e in rail:
    print(e)