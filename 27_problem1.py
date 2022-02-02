__author__ = "Shadman Wadith"
__copyright__ = "Copyright 2022, Cryptography and Network Security Lab Project"
__license__ = "Apache-2.0"
__version__ = "1.0"
__email__ = "wadith.24csedu.027@gmail.com"
__status__ = "Production"

"""
Description :   This following code is for encrypting and decrypting 
                a plain text using Vigenere Cipher Algorithm using a 
                key you want. You can save the plain text in input.txt
                and key in key.txt. The output will be generated in 
                output.txt file with a format of five character group
                with a space
                
Caution :       Here the alphabet dictionary is considered as 
                ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
                which means that A's index value is considered 0 and 
                z's index value is considered 1
                So the encryption might be different from those who 
                considered small letters first                                      
"""

def charValue(char):
    """
        Handy function for mapping every character to a integer value
        :param char: Characters for which I want to
        :return: the integer value of the character
        """
    if 'A' <= char <= 'Z':
        return ord(char) - 65
    elif 'a' <= char <= 'z':
        return ord(char) - 71


def cipherText(string, key):
    """
    This function returns the encrypted text generated
    with the help of the key
    :param string: Plaint text I want to encrypt
    :param key:
    :return: returns cipher text
    """
    cipher_text = []
    key_length = len(key);
    print("key_length : " + str(key_length))
    for i in range(len(string)):
        if i % 5 == 0 and i > 0:
            cipher_text.append(' ')
        string_value = charValue(string[i])
        key_value = charValue(key[i % key_length])
        # x = (ord(string[i]) + ord(key[i % key_length]))
        x = (string_value + key_value) % 52
        if 0 <= x <= 25:
            x += ord('A')
        elif 26 <= x <= 51:
            x += ord('a') - 26
        cipher_text.append(chr(x))
    return ("".join(cipher_text))


def originalText(cipher_text, key):
    """
        This function decrypts the encrypted text
        :param cipher_text:
        :param key:
        :return: original text
        """
    orig_text = []
    key_length = len(key)
    for i in range(len(cipher_text)):
        cipher_value = charValue(cipher_text[i])
        key_value = charValue(key[i % key_length])
        # x = (ord(cipher_text[i]) - ord(key[i % key_length]) + 26) % 26
        x = (cipher_value - key_value + 52) % 52
        if 0 <= x <= 25:
            x += ord('A')
        elif 26 <= x <= 51:
            x += ord('a') - 26
        orig_text.append(chr(x))
    return "".join(orig_text)


def trimText(message):
    """
        This functions cleans the string
        It removes all the characters without A-Z, a-z
        :param message: The string which I want to trim
        :return: returns a string
        """
    trimmed_text = []
    for i in range(len(message)):
        if 'A' <= message[i] <= 'Z' or 'a' <= message[i] <= 'z':
            trimmed_text.append(message[i])
    return "".join(trimmed_text)


def input(message, keyword):
    """
    Handling the input from of the problem
    :param message: Plain text
    :param keyword: key
    :return:
    """
    msg = ""
    for i in range(len(message)):
        msg = msg + message[i]
    # for i in range(len(message)):
    # print(msg)
    string = trimText(msg)
    # print(len(string))
    print("Plaint Text : " + str(string))
    print("Key : " + keyword)
    cipher_text = cipherText(string, keyword)
    output_file.write(cipher_text)
    output_file.write('\n')
    print("Ciphertext :", cipher_text)
    cipher_text = trimText(cipher_text)
    print("Original/Decrypted Text :",
          originalText(cipher_text, keyword))
    print()


if __name__ == "__main__":
    input_file = open("input_1.txt", "r")
    key_file = open("key.txt", "r")
    output_file = open("output.txt", "w+")
    message = input_file.readlines()
    keyword = key_file.readline()
    input(message, keyword)
    input_file.close()
    output_file.close()
    key_file.close()
