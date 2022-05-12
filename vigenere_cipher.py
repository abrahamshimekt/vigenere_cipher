"""
Vigen cipher is one of the simplest that employs a form of poly alphabetic substitution (each letter is assigned
more than one substitute).

It was first described in 1553 but took an entire three centuries to break it in 1863.

Weakness: If someone finds key length then this can be broken.
"""
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("800x400")
window.title("vigenere cipher")
window.iconbitmap(r'C:\Users\simek\Downloads\vigenere_icon.ico')
window.config(bg="gray17")
intro = Label(window, text="Welcome to the vigenere cipher:)",bg="gray17",fg="lime", font=("Arial", 12))
intro.place(x=500, y=10)

message_canvas = Canvas(window,width=400,height=400,bg="teal")
message_canvas.place(x=0,y=0)

message_label = Label(window, text="message :", font=("Arial", 12))
message_label.place(x=20, y=85)

message_entered = Entry(window,borderwidth=7, bg="#d3d3d3", width=30, font=("Arial", 12))
message_entered.place(x=102, y=80)
message_entered.insert(0,"enter your message here")
key_label = Label(window, text="msg_key :", font=("Arial", 12))
key_label.place(x=20, y=135)

key_entered = Entry(window, bg="#d3d3d3",borderwidth=7, width=30, font=("Arial", 12),)
key_entered.place(x=102, y=130)
key_entered.insert(0,"enter your key here")

encrypted_label = Label(window, text="Encrypted :", font=("Arial", 12))
encrypted_label.place(x=420, y=80)

decrypted_label = Label(window, text="Decrypted :", font=("Arial", 12))
decrypted_label.place(x=420, y=130)

encrypted_message = Entry(window, bg="#d3d3d3", width=30, font=("Arial", 12))
encrypted_message.place(x=510, y=80)

decrypted_message = Entry(window, bg="#d3d3d3", width=30, font=("Arial", 12))
decrypted_message.place(x=510, y=130)

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
    is_message_int = False
    is_key_int = False
    for m in message.lower():
        if m not in "abcdefghijklmnopqrstuvwxyz ":
            is_message_int = True
            break
    for k in key.lower():
        if k not in "abcdefghijklmnopqrstuvwxyz ":
            is_key_int = True
            break
    if is_message_int or is_key_int:
        encrypted_message.insert(0, "please use English characters only")
    else:
        encrypted = encrypt(message.lower(), key.lower())
        encrypted_message.insert(0, encrypted)


def display_decrypted():
    message = message_entered.get()
    key = key_entered.get()
    is_message_int = False
    is_key_int = False
    for m in message.lower():
        if m not in "abcdefghijklmnopqrstuvwxyz ":
            is_message_int = True
            break
    for k in key.lower():
        if k not in "abcdefghijklmnopqrstuvwxyz ":
            is_key_int = True
            break
    if is_message_int or is_key_int:
        decrypted_message.insert(0, "please use English characters only")
    else:
        decrypted = decrypt(message.lower(), key.lower())
        decrypted_message.insert(0, decrypted)


def clear():
    encrypted_message.delete(0, END)
    decrypted_message.delete(0, END)


encrypt_button = Button(window, text="Encrypt", width=10, bg="green", command=display_encrypted, font=("Arial", 12))
encrypt_button.place(x=60, y=190)
decrypt_button = Button(window, text="Decrypt", width=10, bg="yellow", command=display_decrypted, font=("Arial", 12))
decrypt_button.place(x=235, y=190)
clear_button = Button(window, text="Clear", width=10, bg="red", command=clear, font=("Arial", 12))
clear_button.place(x=550, y=190)
mainloop()
