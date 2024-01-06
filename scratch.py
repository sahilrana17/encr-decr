import random
import string

original =  string.punctuation + string.digits + string.ascii_letters
chars = list(original)
encr = string.digits + string.ascii_letters + string.punctuation
print(f"chars: {original}")
print(f"key:{encr}")

#encryption
encrypt = input("Enter a message to encrypt: ")
encrypted =" "

for letter in encrypt:
    index = original.index(letter)
    encrypted += encr[index]

print(f"original message {encrypt}")
print(f"encrypted message {encrypted}")

#decryption
encrypted = input("Enter a message to decrypt: ")
encrypt =" "

for letter in encrypted:
    index = encr.index(letter)
    encrypt += original[index]

print(f"original message {encrypted}")
print(f"encrypted message {encrypt}")




