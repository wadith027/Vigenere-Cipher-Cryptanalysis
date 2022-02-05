# Vigenere-Cipher-Cryptanalysis

This is an assignment of Cryptography and Network Security Lab. Here the programs can encrypt an input along with a key given in the input.txt and key.txt file. And the Second problem can predict the key from the given ciphertext. Though it's not 100% accurate.
I have followed these 2 helpful links for cracking the cipher text without the key. I followed Kasiski's method to predict the key. 

* [Vigenere-Cipher](https://www.javatpoint.com/vigenere-cipher#:~:text=The%20vigenere%20cipher%20is%20an%20algorithm%20of%20encrypting%20an%20alphabetic,of%20a%20polyalphabetic%20substitution%20cipher.&text=This%20algorithm%20was%20first%20described%20in%201553%20by%20Giovan%20Battista%20Bellaso.)
* [Vigenere-Cipher-Simulation](https://www.quora.com/How-can-I-crack-the-Vigenere-cipher-without-knowing-the-key?ch=10&oid=13487818&share=063618ec&srid=g4WO0&target_type=question)

## Installation

Just download the project and run 27_problem1.py and 27_problem2.py 

```bash
python 27_problem1.py
python 27_problem2.py
```

## Usage
27_problem1.py is used for encrypting the plain text with the given key in key.txt
27_problem2.py is used for predicting the key from the given ciphertext using Kasiski's algorithm.
Change the input.txt to use different plain text. Use larger plain text for cracking an accurate key from the given cipher text. To use a different key, just change the key.txt file.


