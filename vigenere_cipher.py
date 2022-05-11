"""
Vigen cipher is one of the simplest that employs a form of poly alphabetic substitution (each letter is assigned
more than one substitute).

It was first described in 1553 but took an entire three centuries to break it in 1863.

Weakness: If someone finds key length then this can be broken.
"""
from tkinter import *

window = Tk()
window.geometry("800x400")
window.title("vigenere cipher")
intro = Label(window, text="Welcome to the vigenere cipher", font=("Arial", 12))
message_canva = Canvas(window,width=400,height=400,bg="teal")
message_label = Label(window, text="message :", font=("Arial", 12))
message_entered = Entry(window, bg="grey", width=30, font=("Arial", 12))
key_label = Label(window, text="key :", font=("Arial", 12))
key_entered = Entry(window, bg="grey", width=30, font=("Arial", 12))
encrypted_label = Label(window, text="Encrypted :", font=("Arial", 12))
decrypted_label = Label(window, text="Decrypted :", font=("Arial", 12))
intro.place(x=500, y=10)
message_canva.place(x=0,y=0)
message_label.place(x=10, y=60)
message_entered.place(x=90, y=60)
key_label.place(x=50, y=100)
key_entered.place(x=90, y=100)
encrypted_label.place(x=420, y=60)
encrypted_message = Entry(window, bg="grey", width=30, font=("Arial", 12))
encrypted_message.place(x=510, y=60)
decrypted_label.place(x=420, y=100)
decrypted_message = Entry(window, bg="grey", width=30, font=("Arial", 12))
decrypted_message.place(x=510, y=100)
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
    encrypted_message.insert(0, encrypted)


def display_decrypted():
    message = message_entered.get()
    key = key_entered.get()
    decrypted = decrypt(message, key)
    decrypted_message.insert(0, decrypted)


def clear():
    message_entered.delete(0, END)
    encrypted_message.delete(0, END)
    decrypted_message.delete(0, END)
    key_entered.delete(0, END)


encrypt_button = Button(window, text="Encrypt", width=10, bg="green", command=display_encrypted, font=("Arial", 12))
decrypt_button = Button(window, text="Decrypt", width=10, bg="yellow", command=display_decrypted, font=("Arial", 12))
clear_button = Button(window, text="Decrypt", width=10, bg="red", command=clear, font=("Arial", 12))
encrypt_button.place(x=100, y=140)
decrypt_button.place(x=250, y=140)
clear_button.place(x=580, y=140)
mainloop()
