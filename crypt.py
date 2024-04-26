from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization, hashes, asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
import os
import base64
from tkinter import filedialog
from tkinter import Tk

def encrypt_AES_GCM(msg, password):
    # Gerar uma chave a partir da senha
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=os.urandom(16),
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    aesCipher = Cipher(algorithms.AES(key), modes.GCM(os.urandom(16)))
    encryptor = aesCipher.encryptor()
    ciphertext = encryptor.update(msg) + encryptor.finalize()
    return (ciphertext, encryptor.tag)

def decrypt_AES_GCM(ciphertext, password, tag):
    # Gerar uma chave a partir da senha
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=os.urandom(16),
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    aesCipher = Cipher(algorithms.AES(key), modes.GCM(os.urandom(16), tag))
    decryptor = aesCipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def encrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Criptografar os dados
        ciphertext, tag = encrypt_AES_GCM(data, password)

        # Sobrescrever o arquivo com os dados criptografados
        with open(file_path, 'wb') as f:
            f.write(ciphertext)
    except Exception as e:
        print(f"Erro ao criptografar o arquivo {file_path}: {str(e)}")

def encrypt_folder(folder_path, password):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, password)

def select_folder():
    root = Tk()
    root.withdraw()  # Esconder a janela Tkinter extra
    folder_path = filedialog.askdirectory()  # Mostrar a caixa de diálogo para escolher a pasta
    return folder_path

# Uso
password = b'rodrigo'
folder_path = select_folder()
if folder_path:
    encrypt_folder(folder_path, password)
else:
    print("Nenhuma pasta selecionada.")
