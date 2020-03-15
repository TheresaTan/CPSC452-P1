import numpy as np
from CipherInterface import *

cipherKey = 0


class Railfence(CipherInterface):

    ##########################################
    # Sets the key to use
    # @param key - the key to use
    # @return - True if the key is valid and False otherwise
    ##########################################
    def setKey(self, key):
        global cipherKey
        cipherKey = int(key)
        if cipherKey != 0:
            return True
        return False

    ##########################################
    # Encrypts a plaintext string
    # @param plaintext - the plaintext string
    # @return - the encrypted ciphertext string
    ##########################################
    def encrypt(self, plaintext):
        counter = -1
        encryptedText = ""
        col = int(len(plaintext) / cipherKey)
        if len(plaintext) % cipherKey > 0:
            col += 1
        railfenceMatrix = np.chararray((cipherKey, col))
        railfenceMatrix[:] = '-'
        for x in range(0, len(plaintext)):
            if x % cipherKey == 0:
                counter += 1
            railfenceMatrix[x % cipherKey][counter] = plaintext[x]
        print(railfenceMatrix)
        for list in railfenceMatrix:
            list = list.decode()
            # print(list)
            for letter in list:
                if letter != '-':
                    encryptedText += letter
        print(encryptedText)
        return encryptedText

    ##########################################
    # Decrypts a string of ciphertext
    # @param cipherText - the ciphertext
    # @return - the plaintext
    ##########################################
    def decrypt(self, ciphertext):
        #print("DECRYPT FUNCTION")
        plaintext = ""
        col = int(len(ciphertext) / cipherKey)
        tempText = ciphertext

        leftOverLetters = int(len(ciphertext) % cipherKey)
        print("LEFTOVERLETTERS:")
        print(leftOverLetters)
        if leftOverLetters > 0:
            col += 1
        fromNum = 0
        toNum = col
        decryptList = np.chararray((cipherKey, col))
        decryptList[:] = '-'
        rowCounter = 0
        colCounter = 0
        # put ciphertext in matrix format
        for x in range(0, cipherKey):
          #print("TEMPTEXT")
          #print(tempText[:col])
          
          if leftOverLetters > 0:
            decryptText = tempText[fromNum:toNum]
            leftOverLetters -= 1
            #print("DECRYPT TEXT")
            #print(decryptText)
            for letter in decryptText:
              decryptList[rowCounter][colCounter] = letter
              colCounter += 1
            fromNum += col
            toNum += col

            rowCounter += 1
            colCounter = 0
          else:
            decryptText = ciphertext[fromNum:toNum - 1]
            #print(decryptText)
            #print("DECRYPT TEXT")
            #print(decryptText)
            for letter in decryptText:
              decryptList[rowCounter][colCounter] = letter
              colCounter += 1
            fromNum += col
            toNum += col
            #print("New text")
            #print(tempText)
            rowCounter += 1
            colCounter = 0


        #print(decryptList)
        rowCounter = 0
        colCounter = 0
        # go through each column and add it to the plaintext
        for x in range(0, len(ciphertext)):

            if rowCounter % cipherKey == 0 and rowCounter > 0:
                colCounter += 1
                rowCounter = 0
            if decryptList[rowCounter][colCounter].decode() != '-':
              plaintext += decryptList[rowCounter][colCounter].decode()
            rowCounter += 1
            #print(plaintext)
        #print("PLAINTEXT")
        print(plaintext)
        return plaintext

#Testing functions
#cipher = Railfence()
#cipher.setKey(7)
#cipherText = cipher.encrypt("meetmeafterthetogaparty")
#plainText = cipher.decrypt(cipherText)
