"""
Vigen cipher is one of the simplest that employs a form of poly alphabetic substitution (each letter is assigned
more than one substitute).

It was first described in 1553 but took an entire three centuries to break it in 1863.

Weakness: If someone finds key length then this can be broken.
"""
from tkinter import *

window = Tk()
window.geometry("400x500")
window.title("vigenere cipher")
label = Label(window, text="Welcome to the vigenere cipher")
message_entered = Entry(window, bg="teal", width=40)
key_entered = Entry(window, bg="teal", width=40, )
label.pack()
message_entered.pack()
key_entered.pack()

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def display_encrypted():
    message = message_entered.get()
    key = key_entered.get()
    encrypted = encrypt(message, key)
    encrypted_message = Label(window, text=encrypted)
    encrypted_message.pack()


def display_decrypted():
    message = message_entered.get()
    key = key_entered.get()
    decrypted = decrypt(message, key)
    decrypted_message = Label(window, text=decrypted)
    decrypted_message.pack()


encrypt_button = Button(window, text="Encrypt", command=display_encrypted)
decrypt_button = Button(window, text="Decrypt", command=display_decrypted)
encrypt_button.pack()
decrypt_button.pack()
mainloop()
