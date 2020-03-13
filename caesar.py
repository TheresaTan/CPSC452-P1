import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def setKey(key):
    cipherKey = int(key)
    cipherKey = -cipherKey
    print('key is ' + key)
    return cipherKey

def encrypt(plaintext):

    encryptedText = []
    tempKey = int(cipherKey)
    tempText = list(plaintext)
    caesar = np.roll(alphabet, tempKey)

    for x in range(len(tempText)):
        for y in range(len(alphabet)):
            if tempText[x] == alphabet[y]:
                encryptedText.append(caesar[y])
                break


    encryptedText = ''.join(encryptedText)
    print('ciphertext: ' + encryptedText)
    return encryptedText

def decrypt(cipherText):
    plainText = []
    tempText = list(cipherText)
    tempKey = int(cipherKey)
    caesar = np.roll(alphabet, tempKey)

    for x in range(len(tempText)):
        for y in range(len(alphabet)):
            if tempText[x] == caesar[y]:
                plainText.append(alphabet[y])
                break

    plainText = ''.join(plainText)
    print('plaintext: ' + plainText)
    return plainText

cipherKey = setKey("6")
ciperText = encrypt("whatishappeninghere")
decrypt(ciperText)
