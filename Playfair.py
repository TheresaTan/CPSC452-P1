import numpy as np
from CipherInterface import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
playfairMatrix = np.chararray((5, 5))


################################################
# Splits text into appropriate pairs
# @param text - the string to split up
# @return - the split text arranged into an array
################################################
def splitText(text):
    pair = ""
    splitList = []
    splitText = ""
    for letter in text:
        if (pair == ""):
            pair += letter
        else:
            if letter == pair:
                pair += 'x'
                splitList.append(pair)
                pair = letter
            else:
                pair += letter
                splitList.append(pair)
                pair = ""
    if pair != "":
        pair += 'x'
        splitList.append(pair)
        pair = ""
    return splitList


class Playfair(CipherInterface):
    ################################################
    # Sets the key to use
    # @param key - the key to use
    # @return - True if the key is valid and False otherwise
    ################################################
    def setKey(self, key):
        global alphabet
        tempList = alphabet
        row = 0
        col = 0

        for letter in key:
            if col > 4:
                row += 1
                col = 0
            if (letter in tempList):
                playfairMatrix[row][col] = letter
                tempList.remove(letter)
                if (letter == 'i'):
                    tempList.remove('j')
                elif (letter == 'j'):
                    tempList.remove('i')
                    # accounts for the i/j space in playfair matrix
                    playfairMatrix[row][col] = 'i'
                col += 1
        for letter in tempList:
            if col > 4:
                row += 1
                col = 0
            if (letter == 'i'):
                tempList.remove('j')
            elif (letter == 'j'):
                tempList.remove('i')
                playfairMatrix[row][col] = 'i'
            playfairMatrix[row][col] = letter
            col += 1

        print(playfairMatrix)
        if playfairMatrix != "":
            return True
        return False

    ################################################
    # Encrypts a plaintext string
    # @param plaintext - the plaintext string
    # @return - the encrypted ciphertext string
    ###############################################
    def encrypt(self, plaintext):
        firstRow = 0
        firstCol = 0
        secondRow = 0
        secondCol = 0
        encryptedText = ""
        foundFirst = False
        foundSecond = False
        splittedText = splitText(plaintext)
        #print(splittedText)
        for pair in splittedText:
            # changes j to i so that it can be found in matrix
            firstLetter = pair[0]
            secondLetter = pair[1]
            if pair[0] == 'j':
                firstLetter = 'i'
            elif pair[1] == 'j':
                secondLetter = 'i'
            while foundFirst == False:
                if playfairMatrix[firstRow][firstCol].decode() == firstLetter:
                    foundFirst = True
                elif firstCol < 4:
                    firstCol += 1
                else:
                    firstRow += 1
                    firstCol = 0
            while foundSecond == False:
                if playfairMatrix[secondRow][secondCol].decode() == secondLetter:
                    foundSecond = True
                elif secondCol < 4:
                    secondCol += 1
                else:
                    secondRow += 1
                    secondCol = 0
            #print("First letter: " + pair[0] + " found at Matrix[", end='')
            #print(firstRow, end='')
            #print("][", end='')
            #print(firstCol, end='')
            #print("]")
            #print("Second letter: " + pair[1] + " found at Matrix[", end='')
            #print(secondRow, end='')
            #print("][", end='')
            #print(secondCol, end='')
            #print("]")

            if (firstRow == secondRow):
                if (firstCol < 4 and secondCol < 4):
                    encryptedText += playfairMatrix[firstRow][firstCol + 1].decode() + playfairMatrix[secondRow][
                        secondCol + 1].decode()
                elif firstCol == 4:
                    encryptedText += playfairMatrix[firstRow][0].decode() + playfairMatrix[secondRow][
                        secondCol + 1].decode()
                elif secondCol == 4:
                    encryptedText += playfairMatrix[firstRow][firstCol + 1].decode() + playfairMatrix[secondRow][
                        0].decode()
            elif (firstCol == secondCol):
                if (firstRow < 4 and secondRow < 4):
                    encryptedText += playfairMatrix[firstRow + 1][firstCol].decode() + playfairMatrix[secondRow + 1][
                        secondCol].decode()
                elif firstRow == 4:
                    encryptedText += playfairMatrix[0][firstCol].decode() + playfairMatrix[secondRow + 1][
                        secondCol].decode()
                elif secondRow == 4:
                    encryptedText += playfairMatrix[firstRow + 1][firstCol].decode() + playfairMatrix[0][
                        secondCol].decode()
            else:
                encryptedText += playfairMatrix[firstRow][secondCol].decode() + playfairMatrix[secondRow][
                    firstCol].decode()

            #print(encryptedText)
            firstRow = 0
            firstCol = 0
            secondRow = 0
            secondCol = 0
            foundFirst = False
            foundSecond = False
        print(encryptedText)
        return encryptedText

    ################################################
    # Decrypts a string of ciphertext
    # @param cipherText - the ciphertext
    # @return - the plaintext
    ################################################
    def decrypt(self, cipherText):
        firstRow = 0
        firstCol = 0
        secondRow = 0
        secondCol = 0
        plainText = ""
        foundFirst = False
        foundSecond = False
        splittedText = splitText(cipherText)
        #print(splittedText)
        for pair in splittedText:
            while foundFirst == False:
                if playfairMatrix[firstRow][firstCol].decode() == pair[0]:
                    foundFirst = True
                elif firstCol < 4:
                    firstCol += 1
                else:
                    firstRow += 1
                    firstCol = 0
            while foundSecond == False:
                if playfairMatrix[secondRow][secondCol].decode() == pair[1]:
                    foundSecond = True
                elif secondCol < 4:
                    secondCol += 1
                else:
                    secondRow += 1
                    secondCol = 0
            #print("First letter: " + pair[0] + " found at Matrix[", end='')
            #print(firstRow, end='')
            #print("][", end='')
            #print(firstCol, end='')
            #print("]")
            #print("Second letter: " + pair[1] + " found at Matrix[", end='')
            #print(secondRow, end='')
            #print("][", end='')
            #print(secondCol, end='')
            #print("]")
            if (firstRow == secondRow):
                if (firstCol > 0 and secondCol > 0):
                    plainText += playfairMatrix[firstRow][firstCol - 1].decode() + playfairMatrix[secondRow][
                        secondCol - 1].decode()
                elif firstCol == 0:
                    plainText += playfairMatrix[firstRow][4].decode() + playfairMatrix[secondRow][
                        secondCol - 1].decode()
                elif secondCol == 0:
                    plainText += playfairMatrix[firstRow][firstCol - 1].decode() + playfairMatrix[secondRow][4].decode()
            elif (firstCol == secondCol):
                if (firstRow < 0 and secondRow < 0):
                    plainText += playfairMatrix[firstRow - 1][firstCol].decode() + playfairMatrix[secondRow - 1][
                        secondCol].decode()
                elif firstRow == 0:
                    plainText += playfairMatrix[4][firstCol].decode() + playfairMatrix[secondRow - 1][
                        secondCol].decode()
                elif secondRow == 0:
                    plainText += playfairMatrix[firstRow - 1][firstCol].decode() + playfairMatrix[4][secondCol].decode()
            else:
                plainText += playfairMatrix[firstRow][secondCol].decode() + playfairMatrix[secondRow][firstCol].decode()
            #print(plainText)
            firstRow = 0
            firstCol = 0
            secondRow = 0
            secondCol = 0
            foundFirst = False
            foundSecond = False
        # This gives both options of I or J when decrypting a text
        if 'i' in plainText:
            tempText = plainText
            plainText += " OR ("
            for letter in tempText:
                if letter == 'i':
                    plainText += 'j'
                else:
                    plainText += letter
            plainText += ")"

        print(plainText)

        return plainText

# Example used to check functions
# cipher = Playfair()
# cipher.setKey("occurrence")
# cipherText = cipher.encrypt("helloworld")
# cipher.decrypt(cipherText)



