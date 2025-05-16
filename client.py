import socket
from Crypto.Cipher import DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64


def start_client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Marrim çelësin publik të serverit
        server_public_key = s.recv(2048)
        rsa_key = RSA.import_key(server_public_key)
        rsa_cipher = PKCS1_OAEP.new(rsa_key)

        # Gjenerojmë një çelës DES dhe IV
        des_key = get_random_bytes(8)  # DES përdor çelësa 64-bit (8 bytes)
        iv = get_random_bytes(8)  # IV duhet të jetë 8 bytes për DES

        # Kriptojmë çelësin DES dhe IV duke përdorur çelësin publik të serverit
        encrypted_des_key = rsa_cipher.encrypt(des_key)
        encrypted_iv = rsa_cipher.encrypt(iv)

        # Dërgojmë çelësin e kriptuar DES dhe IV te serveri
        s.sendall(encrypted_des_key)
        s.sendall(encrypted_iv)

        # Krijojmë cipher DES
        des_cipher = DES.new(des_key, DES.MODE_CBC, iv)