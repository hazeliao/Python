#-------------------------------------------------------------------------------
#
# The purpose of this file is to exercise some Python via basic cryptology.
#
#-------------------------------------------------------------------------------

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET += ALPHABET.upper() + ' .,!?'

def encrypt(msg, shift):
    newmsg = ""
    for i in range(len(msg)):
        newmsg += ALPHABET[(ALPHABET.find(msg[i]) + shift%57)%57]
    return newmsg
        
def decrypt(encrypted_msg, shift):
    newmsg =''
    for i in range(len(encrypted_msg)):
        newmsg += ALPHABET[(ALPHABET.find(encrypted_msg[i]) - shift%57)%57]
    return newmsg

