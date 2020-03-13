from CipherInterface import CipherInterface
from Playfair import Playfair
from Vigenere import Vigenere
import sys
#######################################
# Enact ciphers
#######################################
def main(argv):
  # Create instance of the CipherInterface
  cipher = CipherInterface()
  if len(argv) < 6:
    print("ERROR: not enough arguments filled out")
  else:
    cipherName = argv[1]
    key = argv[2]
    encOrDec = argv[3]
    textInput = argv[4] + ".txt"
    textOutput = argv[5] + ".txt"
    print(cipherName)
    print(key)
    print(encOrDec)
    print(textInput)
    print(textOutput)

  # Open inputfile to read contents
  # assign contents to variable to encrypt/decrypt
  inputFile = open(textInput, "rt")
  contents = inputFile.read()
  inputFile.close()
  #print("File Contents")
  #print(contents)

  #Choose the cipher
  if cipherName.lower() == "plf":
    print("Playfair is chosen")
    cipher = Playfair()
    # Set the encryption key
    cipher.setKey(key)
    if(encOrDec.lower() == "enc"):
      # Perform encryption
      outputText = cipher.encrypt(contents)
    else:
      # Perform decryption
      outputText = cipher.decrypt(contents)
    # Create and write into output file the outputText
    outputFile = open(textOutput,"w+")
    outputFile.write(outputText)
    outputFile.close()
  elif cipherName.lower() == "vig":
    print("Vigenere is chosen")
    cipher = Vigenere()
    # Set the encryption key
    cipher.setKey(key)
    if(encOrDec.lower() == "enc"):
      # Perform encryption
      outputText = cipher.encrypt(contents)
    else:
      # Perform decryption
      outputText = cipher.decrypt(contents)
    # Create and write into output file the outputText
    outputFile = open(textOutput,"w+")
    outputFile.write(outputText)
    outputFile.close()
    

main(sys.argv)

  

