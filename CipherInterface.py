#############################################
# This class implements the interface for a typical cipher.
# It defines functions usually used in a cipher
#############################################
class CipherInterface:

    ############################################
    # Sets the key to use
    # @param key - the key to use
    # @return - True if the key is valid and False otherwise
    #############################################
    def setKey(self,key):
      return False

    ##################################################
    # Encrypts a plaintext string
    # @param plaintext - the plaintext string
    # @return - the encrypted ciphertext string
    ##################################################
    def encrypt(self,plaintext):
      return ""

    ###################################################
    # Decrypts a string of ciphertext
    # @param ciphertext - the ciphertext
    # @return - the plaintext
    ###################################################
    def decrypt(self,ciphertext):
      return ""

# Example to check functions
#cipher = CipherInterface()
#text = cipher.setKey(1)
