__author__ = "Shadman Wadith"
__copyright__ = "Copyright 2022, Cryptography and Network Security Lab Project"
__license__ = "Apache-2.0"
__version__ = "1.0"
__email__ = "wadith.24csedu.027@gmail.com"
__status__ = "Production"

"""
Description :   This following code is for predicting the key from the given
                cipher text without knowing the actual key. Here I tried to
                implement Kasiski's Method.Here is the Kasiski's method and
                it's simulation in the following link 
                https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Kasiski.html
                https://www.quora.com/How-can-I-crack-the-Vigenere-cipher-without-knowing-the-key?ch=10&oid=13487818&share=063618ec&srid=g4WO0&target_type=question  
                 
Caution :       Here the alphabet dictionary is considered as 
                ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
                which means that A's index value is considered 0 and 
                z's index value is considered 1
                So the encryption might be different from those who 
                considered small letters first.
                
                And the following keyword will be just opposite( A => a)
                if that indexing of alphabet is followed                   
"""
def find_all(a_str, sub, s_index):
    """
    This is a function for finding all the matched substring from given string
    :param a_str: It's main string
    :param sub: It's the substring
    :param s_index: Index of the string from where the searching starts
    :return: Index of that particular substring
    """
    start = s_index
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1


def charValue(char):
    """

    :param char: Characters for which I want to
    :return: the integer value of the character
    """
    if 'A' <= char <= 'Z':
        return ord(char) - 65
    elif 'a' <= char <= 'z':
        return ord(char) - 71


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


# Function for predicting key length
def predictKeyLength(cipher_text):
    distance = [] # For the distance between the tri-graphs of the cipher text
    factors = [] # stores all the factor of the distance
    key_lengths = [] # possible key lengths

    # initializing factors array up to 21 size
    # We assume that our key can be of size 20
    for i in range(21):
        factors.append(0)
    for index in range(len(cipher_text) - 2):
        sub_strs = list(find_all(cipher_text, cipher_text[index: index + 3], index))
        if len(sub_strs) > 1:
            for i in range(len(sub_strs) - 1):
                distance_var = sub_strs[i + 1] - sub_strs[0]
                if distance_var not in distance:
                    distance.append(distance_var)
    distance.sort()
    # print("Distance Array :")
    # print(distance)
    for i in range(4,21):
        for j in range(len(distance)):

            if distance[j] % i == 0:
                factors[i] += 1
    # print("Factors Count : ")
    # print(factors)
    maximum_factor = max(factors)
    error = maximum_factor * .15
    for factor in factors:
        if factor > maximum_factor - error:
            key = factors.index(factor)
            key_lengths.append(key)
    return key_lengths


# This is function act like hacking caesar cipher
# This generates the possible letters from a given string sequence
def possibleLetters(string):
    letter_frequency = []
    letters = []
    # Initializing list
    for i in range(52):
        letter_frequency.append(0)
    for i in range(len(string)):
        letter_index = charValue(string[i])
        letter_frequency[letter_index] += 1
    # It stores two letter prediction
    for i in range(2):
        # here index is the position of english alphabets starting from A
        maximum_frequency = max(letter_frequency)
        maximum_frequency_index = letter_frequency.index(maximum_frequency)
        if maximum_frequency_index < 26:
            letter_frequency[maximum_frequency_index] = 0
            maximum_frequency_index = maximum_frequency_index - 4  # As shift of e is 4
            if maximum_frequency_index < 0:
                letter = chr(ord('A') + (maximum_frequency_index + 26))
            else:
                letter = chr(ord('a') + maximum_frequency_index)
            letters.append(letter)
        else:
            letter_frequency[maximum_frequency_index] = 0
            maximum_frequency_index -= 26
            maximum_frequency_index = maximum_frequency_index - 4 # As shift of e is 4
            if maximum_frequency_index < 0:
                letter = chr(ord('a') + (maximum_frequency_index + 26))
            else:
                letter = chr(ord('A') + maximum_frequency_index)
            letters.append(letter)

    # print(letters)
    return letters


def predictKey(cipher_text, key_length):
    text_level = [] # This stores every key_length position into different list
    keys = []
    for i in range(key_length):
        text_level.append("")
    for i in range(len(cipher_text)):
        text_level[i % key_length] += cipher_text[i]
    # print(text_level)
    for i in range(key_length):

        keys.append(possibleLetters(text_level[i]))
    predicted_key = ""
    for key in keys:
        predicted_key += key[0]
    print("Key Length     : " + str(key_length))
    print("Predicted Key  : " + predicted_key)
    return predicted_key


# Handy function to calculate the accuracy of key
def calculateAccuracy(plain_text, deciphered_text):
    count = 0
    msg_length = len(plain_text)
    for i in range(msg_length):
        if plain_text[i] == deciphered_text[i]:
            count += 1
    accuracy = (count*100)/msg_length
    return accuracy


def plainText(message):
    msg = ""
    for i in range(len(message)):
        msg = msg + message[i]
    # for i in range(len(message)):
    msg = trimText(msg)
    return msg


def decrypt(cipher):
    cipher_text = ""
    for i in range(len(cipher)):
        string = trimText(cipher[i])
        cipher_text = cipher_text + string
    key_lengths = predictKeyLength(cipher_text)
    for key in key_lengths:
        key = predictKey(cipher_text, key)
        # print(key)
        predicted_text = originalText(cipher_text, key)
        accuracy = calculateAccuracy(plain_text, predicted_text)
        print("Predicted text : " + predicted_text)
        print("Plain text     : " + plain_text)
        print("Accuracy       : " + str(round(accuracy, 2)) + "%")
        print()

    
# Driver code
if __name__ == "__main__":
    f_let = []
    input_file = open("input_1.txt", "r")
    key_file = open("key.txt", "r")
    output_file = open("output.txt", "r")
    message = input_file.readlines()
    plain_text = plainText(message)
    keyword = key_file.readline()
    cipher = output_file.readlines()
    decrypt(cipher)
    print("Actual key     : " + keyword)
    input_file.close()
    output_file.close()
    key_file.close()

