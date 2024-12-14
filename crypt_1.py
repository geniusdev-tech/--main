import os

from tkinter import filedialog, Tk, Button, Label, Entry, StringVar, Frame, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Função para encriptar usando AES-GCM
def encrypt_AES_GCM(msg, password):
    salt = os.urandom(16)
    nonce = os.urandom(12)  # Nonce de 12 bytes (96 bits)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    key = kdf.derive(password)
    
    aesCipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = aesCipher.encryptor()
    ciphertext = encryptor.update(msg) + encryptor.finalize()
    
    return salt, nonce, ciphertext, encryptor.tag[:16]  # Garantir que a tag seja de 16 bytes

# Função para desencriptar usando AES-GCM
def decrypt_AES_GCM(salt, nonce, ciphertext, password, tag):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000)
    key = kdf.derive(password)
    
    aesCipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = aesCipher.decryptor()
    
    return decryptor.update(ciphertext) + decryptor.finalize()

# Função para o botão de encriptar
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
        f.write(salt + b' ' + nonce + b' ' + ciphertext + b' ' + tag)
    
    messagebox.showinfo("Success", "File encrypted successfully!")

# Função para o botão de desencriptar
def decrypt_button_clicked():
    password = password_entry.get().encode()
    if password != b'password':
        messagebox.showwarning("Atenção", "Senha incorreta!")
        return
    
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as f:
        data = f.read()
    
    try:
        salt, nonce, ciphertext, tag = data.split(b' ', 3)
    except ValueError:
        messagebox.showerror("Error", "O arquivo parece estar corrompido ou no formato errado.")
        return
    
    try:
        plaintext = decrypt_AES_GCM(salt, nonce, ciphertext, password, tag)
    except Exception as e:
        messagebox.showerror("Error", f"Falha na desencriptação: {e}")
        return
    
    with open(file_path, 'wb') as f:
        f.write(plaintext)
    
    messagebox.showinfo("Success", "File decrypted successfully!")

# Configuração da interface gráfica com Tkinter
def setup_gui():
    root = Tk()
    root.geometry("300x150")
    
    Label(root, text="Password").pack()
    global password_entry
    password_entry = Entry(root, textvariable=StringVar())
    password_entry.pack()
    
    frame = Frame(root)
    frame.pack()
    
    Button(frame, text="Encrypt", command=encrypt_button_clicked).pack(side="left")
    Button(frame, text="Decrypt", command=decrypt_button_clicked).pack(side="left")
    
    root.mainloop()

# Inicializar a GUI
setup_gui()
