# Detyra3_DSfinal
This project was made for assignment in Data Security class 2025
# Project Description
This project implements a secure client-server communication system using TCP sockets where:

Data exchanged between applications is encrypted using DES-CBC (Data Encryption Standard in Cipher Block Chaining mode)

The secret key is protected using public key cryptography
# Features
Secure encrypted communication channel between client and server

Hybrid encryption approach:

Symmetric encryption (DES-CBC) for message confidentiality

Asymmetric encryption (RSA) for secure key exchange

One-way communication (client to server only)

Protection against eavesdropping and man-in-the-middle attacks

# Technical Specifications
# Encryption Protocols
# Key Exchange:

Server generates RSA key pair (public/private)

Client receives server's public key

Client generates DES secret key

Client encrypts DES key with server's public key and sends it to server

Server decrypts DES key with its private key

# Message Encryption:

All subsequent messages are encrypted with DES-CBC

Each message includes proper initialization vector (IV) for CBC mode

# Communication Flow
Server starts and waits for connections

Client connects to server

Key exchange occurs (as described above)

Client sends encrypted messages to server

Server decrypts and processes messages
# Requirements
Python 3.x

Cryptography libraries (PyCryptodome recommended)

Socket programming capabilities
# Security Considerations
The server must protect its private key

DES is used here for educational purposes - in production consider AES

Proper IV generation and management is crucial for CBC security

No authentication mechanism is implemented in this basic version
