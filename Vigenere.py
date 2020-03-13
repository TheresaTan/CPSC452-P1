import numpy as np
from CipherInterface import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
cipherKey = ""


class Vigenere(CipherInterface):

    ##########################################
    # Sets the key to use
    # @param key - the key to use
    # @return - True if the key is valid and False otherwise
    ##########################################
    def setKey(self, key):
        global cipherKey
        cipherKey = key
        #print(cipherKey)
        if cipherKey == "":
            return False
        return True

    ##########################################
    # Encrypts a plaintext string
    # @param plaintext - the plaintext string
    # @return - the encrypted ciphertext string
    ##########################################
    def encrypt(self, plaintext):
        global alphabet
        counter = 0
        tempKey = cipherKey
        encryptedText = ""
        plainIndex = 0
        keyIndex = 0
        encryptIndex = 0
        while len(plaintext) > len(tempKey):
            tempKey += cipherKey[counter]
            if counter < len(cipherKey) - 1:
                counter += 1
            else:
                counter = 0
        #print(plaintext, end='')
        #print(" Length: ", end='')
        #print(len(plaintext))
        #print(tempKey, end='')
        #print(" Length: ", end='')
        #print(len(tempKey))
        for x in range(0, len(plaintext)):
            plainIndex = alphabet.index(plaintext[x])
            keyIndex = alphabet.index(tempKey[x])
            encryptIndex = plainIndex + keyIndex
            if encryptIndex >= len(alphabet):
                encryptIndex -= len(alphabet)

            #print(encryptIndex)
            encryptedText += alphabet[encryptIndex]
            #print(encryptedText)
        print(encryptedText)
        return encryptedText

    ##########################################
    # Decrypts a string of ciphertext
    # @param cipherText - the ciphertext
    # @return - the plaintext
    ##########################################
    def decrypt(self, ciphertext):
        global alphabet
        counter = 0
        tempKey = cipherKey
        plainText = ""
        cipherIndex = 0
        keyIndex = 0
        plainIndex = 0
        while len(ciphertext) > len(tempKey):
            tempKey += cipherKey[counter]
            if counter < len(cipherKey) - 1:
                counter += 1
            else:
                counter = 0
        #print(ciphertext, end='')
        #print(" Length: ", end='')
        #print(len(ciphertext))
        #print(tempKey, end='')
        #print(" Length: ", end='')
        #print(len(tempKey))
        for x in range(0, len(ciphertext)):
            cipherIndex = alphabet.index(ciphertext[x])
            keyIndex = alphabet.index(tempKey[x])
            plainIndex = cipherIndex - keyIndex
            if plainIndex < 0:
                plainIndex += len(alphabet)

            #print(plainIndex)
            plainText += alphabet[plainIndex]
            #print(plainText)
        print(plainText)
        return plainText


# Examples to check functions
#cipher = Vigenere()
#cipher.setKey("deceptive")
#cipherText = cipher.encrypt("wearediscoveredsaveyourself")
#cipher.decrypt(cipherText)
