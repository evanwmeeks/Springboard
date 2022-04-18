"""
Function grabs user input when ran to select a string to encrypt and value to shift by. 
Tests for ASCII characters, effectively including everything on an English keyboard. 
Tests for out of range characters and returns 'Invalid Input' if found
Returns encrypted string. 

I seem to get whitespace as an output character very frequently, and I cannot figure out why. 
(or something is throwing off character counts and I'm mistaking their absence as whitespace)

Was the '.isascii()' function the correct choice, or was I supposed to iterate through Caps/lower
and punctuation individually for this project?


Code inspired by: https://note.nkmk.me/en/python-str-num-determine/ and 
https://likegeeks.com/python-caesar-cipher/

"""
string = input("What would you like to encrypt? ")
shift = input("Choose a shift value: ")

def c_cipher(string, shift):
    num = int(shift)
    string1 = str(string)
    encrypted_unicode=' '
    for i in string1:
        if i.isascii():
            temp = (ord(i) + num)
            encrypted_unicode = encrypted_unicode + chr(temp)
        else:
            return "Invalid Input"
    return "Your Cipher is: " + str(encrypted_unicode)

print(c_cipher(string, shift))
