# Christopher Phongsa
# 3/12/2020

import random
import math
from CipherInterface import *

cipherKey = ""
ciphertext = ""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
class RowTransposition(CipherInterface):

    ########################################################
    # Sets the key to use
    # @param key - the key to use
    # @return - True if the key is valid and False otherwise
    ########################################################
    def setKey(self, key):
        global cipherKey
        cipherKey = key
        if cipherKey == "":
            return False
        return True

    ########################################################
    # Encrypts a plaintext string
    # @param plaintext - plaintext string
    # @param cipherKey - key to encrypt plaintext
    # @return - encrypted ciphertext key
    ########################################################
    def encrypt(self, plaintext):

        global alphabet 
        global ciphertext

        col = len(cipherKey)
        row = math.ceil(len(plaintext)/col)
        # counter to check when we finishing iterating through the plaintext
        counter = 0

        # initialize temp to 0
        temp = [[0 for x in range(col)] for y in range(row)]
        
        # prints out the matrix so you may check for successful initialization
        for i in range(0, row):
            if i > 0:
                print("")
            for j in range(0, col):
                print(temp[i][j], end=" ")
        print("")

        # enters plaintext into matrix
        for i in range(0, row):
            for j in range(0, col):
                if counter < len(plaintext):
                    temp[i][j] = plaintext[counter]
                    counter += 1
                else:
                    # once the plaintext has been filled into the matrix, 
                    # we add arbitrary alphabet letters to the remaining slots in the matrix
                    temp[i][j] = alphabet[random.randrange(0, 24, 1)]

        # prints out the array so you may be able to check it
        for i in range(0, row):
            if i > 0:
                print("")
            for j in range(0, col):
                print(temp[i][j], end=" ")

        print("\n")
        
        #Encrypt plaintext to ciphertext
        for i in range(col):
            idx = int(cipherKey[i])-1
            # for each row in temp, you will add the value, according to the respective column number
            ciphertext += "".join([row[idx] for row in temp])
                
        print(ciphertext)

        return ciphertext

# Examples to check functions
cipher = RowTransposition()
cipher.setKey("3124")
ciphertext = cipher.encrypt("thisisatest")

    