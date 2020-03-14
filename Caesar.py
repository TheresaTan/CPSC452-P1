import numpy as np
from CipherInterface import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipherKey = ""
class Caesar(CipherInterface):
  ################################################
  # Sets the key to use
  # @param key - the key to use
  # @return - True if the key is valid and False otherwise
  ################################################
  def setKey(self,key):
    global cipherKey
    cipherKey = int(key)
    cipherKey = -cipherKey
    print('key is ' + key)
    if cipherKey != "":
      return True
    return False

  ################################################
  # Encrypts a plaintext string
  # @param plaintext - the plaintext string
  # @return - the encrypted ciphertext string
  ###############################################
  def encrypt(self,plaintext):

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

  ################################################
  # Decrypts a string of ciphertext
  # @param cipherText - the ciphertext
  # @return - the plaintext
  ################################################
  def decrypt(self,cipherText):
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

#Testing functions example
#cipher = Caesar()
#cipher.setKey("6")
#ciperText = cipher.encrypt("whatishappeninghere")
#cipher.decrypt(ciperText)
