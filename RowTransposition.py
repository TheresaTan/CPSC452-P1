# Christopher Phongsa - Encryption
# Andrew Lopez - Decryption
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
        print("\n")

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
        print("\n")

        return ciphertext
    ########################################################
    # Decrypts a plaintext string
    # @param cipherText - ciphertext string
    # @return - plaintext
    ########################################################
    def decrypt(self,ciphertext):
        global alphabet 
        global cipherKey
        decplaintext = ""

        col = len(cipherKey)
        row = math.ceil(len(ciphertext)/col)

        temp = [[0 for x in range(col)] for y in range(row)]
        counter = 0

        # prints out the matrix so you may check for successful initialization
        for i in range(0, row):
            if i > 0:
                print("")
            for j in range(0, col):
                print(temp[i][j], end=" ")
        print("\n")

        # makes matrix with ciphertext inputed
        for x in range(0, col):
            for y in range(0, row):
                temp[y][x] = ciphertext[counter]
                counter += 1
        #check ciphertext was inputed correctly
        for i in range(0, row):
            if i > 0:
                print("")
            for j in range(0, col):
                print(temp[i][j], end=" ")
        print("\n")
 

        #this will create a new matrix with columns reoragnized to key
        decCipher = [[0 for x in range(col)] for y in range(row)]
        for x in range(0, col):
            for y in range(0, row):
                decCipher[y][int(cipherKey[x])-1] = temp[y][x]

        #prints new matrix for check
        for i in range(0, row):
            if i > 0:
                print("")
            for j in range(0, col):
                print(decCipher[i][j], end=" ")
        print("\n")

        #decrypt ciphertext to plaintext
        for i in range(0, row):
            for j in range(0, col):
            # for each row in temp, you will add the value, according to the respective column number
                decplaintext += decCipher[i][j]
        
        print(decplaintext)
        

# Examples to check functions
cipher = RowTransposition()
cipher.setKey("3124")
cipherText = cipher.encrypt("thisisatest")
cipher.decrypt(cipherText)

    