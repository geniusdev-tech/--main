from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes, asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
import os
import base64
from tkinter import filedialog, Tk, Button, Label, Entry, StringVar, Frame, messagebox

def encrypt_AES_GCM(msg, password):
    salt = os.urandom(16)
    nonce = os.urandom(16)

    # Gerar uma chave a partir da senha e do salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)

    aesCipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = aesCipher.encryptor()
    ciphertext = encryptor.update(msg) + encryptor.finalize()

    # Retorna o salt, o nonce, o texto cifrado e o tag
    return (salt, nonce, ciphertext, encryptor.tag)

def decrypt_AES_GCM(salt, nonce, ciphertext, password, tag):
    # Gerar uma chave a partir da senha e do salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)

    aesCipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = aesCipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def encrypt_button_clicked():
    password = password_entry.get().encode()
    if password != b'password':
        messagebox.showwarning("Atenção", "Senha incorreta!")
        return
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as f:
        data = f.read()
    salt, nonce, ciphertext, tag = encrypt_AES_GCM(data, password)
    with open(file_path, 'wb') as f:
        f.write(b' '.join([salt, nonce, ciphertext, tag]))
    messagebox.showinfo("Success", "File encrypted successfully!")

def decrypt_button_clicked():
    password = password_entry.get().encode()
    if password != b'password':
        messagebox.showwarning("Atenção", "Senha incorreta!")
        return
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as f:
        salt, nonce, ciphertext, tag = f.read().split(b' ')
    plaintext = decrypt_AES_GCM(salt, nonce, ciphertext, password, tag)
    with open(file_path, 'wb') as f:
        f.write(plaintext)
    messagebox.showinfo("Success", "File decrypted successfully!")

root = Tk()
root.geometry("300x150")

password_label = Label(root, text="Password")
password_label.pack()
password_entry = Entry(root, textvariable=StringVar())
password_entry.pack()

frame = Frame(root)
frame.pack()

encrypt_button = Button(frame, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.pack(side="left")

decrypt_button = Button(frame, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack(side="left")

root.mainloop()
