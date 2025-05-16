import socket
import threading
from Crypto.Cipher import DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
import base64

# Gjenerojmë çelësat RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Ruajmë çelësat në skedarë (për demonstrim)
with open('server_private.pem', 'wb') as f:
    f.write(private_key)
with open('server_public.pem', 'wb') as f:
    f.write(public_key)


def handle_client(conn):
    try:
        # Dërgojmë çelësin publik të serverit te klienti
        conn.sendall(public_key)

        # Marrim çelësin e DES të kriptuar me RSA
        encrypted_des_key = conn.recv(2048)

        # Dekriptojmë çelësin DES duke përdorur çelësin privat të serverit
        rsa_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
        des_key = rsa_cipher.decrypt(encrypted_des_key)

        # Marrim IV-në e kriptuar
        encrypted_iv = conn.recv(2048)
        iv = rsa_cipher.decrypt(encrypted_iv)
