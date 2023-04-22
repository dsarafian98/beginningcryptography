# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:28:04 2020

@author: Danielle Sarafian
"""

#!/usr/bin/python3
# FOR TRAINING USE ONLY! DO NOT USE THIS FOR REAL CRYPTOGRAPHY

import os, binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#### DANGER ####
# The following RSA encryption and decryption is
# completely unsafe and terribly broken. DO NOT USE
# for anything other than the practice exercise
################
def simple_rsa_encrypt(m, publickey):
    return publickey.encrypt(m, padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),label=None))

def simple_rsa_decrypt(c, privatekey):
    return privatekey.decrypt(c, padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),label=None))
  
#### DANGER ####

def int_to_bytes(i):
    # i might be a gmpy2 big integer; convert back to a Python int
    i = int(i)
    return i.to_bytes((i.bit_length()+7)//8, byteorder='big')

def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')

def main():
    public_key_file = None
    private_key_file = None
    public_key = None
    private_key = None
    while True:
        print("Simple RSA Crypto")
        print("--------------------")
        print("\tprviate key file: {}".format(private_key_file))
        print("\tpublic key file: {}".format(public_key_file))
        print("\t1. Encrypt Message.")
        print("\t2. Decrypt Message.")
        print("\t3. Load public key file.")
        print("\t4. Load private key file.")
        print("\t5. Create and load new public and private key files.")
        print("\t6. Encrypt, Multiply, and Decrypt Messages")
        print("\t7. Quit.\n")
        choice = input(">> ")
        if choice == '1':
            if not public_key:
                print("\nNo public key loaded\n")
            else:
                message = input("\nPlaintext: ").encode()
                cipher = simple_rsa_encrypt(message, public_key)
                print("\nCiphertext (hexlified): {}\n".format(binascii.hexlify(cipher)))
        elif choice == '2':
            if not private_key:
                print("\nNo private key loaded\n")
            else:
                cipher_hex = input("\nCiphertext (hexlified): ").encode()
                cipher = binascii.unhexlify(cipher_hex)
                message = simple_rsa_decrypt(cipher, private_key)
                
                print("\nPlaintext: {}\n".format(message))
        elif choice == '3':
            public_key_file_temp = input("\nEnter public key file: ")
            if not os.path.exists(public_key_file_temp):
                print("File {} does not exist.")
            else:
                with open(public_key_file_temp, "rb") as public_key_file_object:
                    public_key = serialization.load_pem_public_key(
                                     public_key_file_object.read(),
                                     backend=default_backend())
                    public_key_file = public_key_file_temp
                    print("\nPublic Key file loaded.\n")

                    # unload private key if any
                    private_key_file = None
                    private_key = None
        elif choice == '4':
            private_key_file_temp = input("\nEnter private key file: ")
            if not os.path.exists(private_key_file_temp):
                print("File {} does not exist.")
            else:
                with open(private_key_file_temp, "rb") as private_key_file_object:
                    private_key = serialization.load_pem_private_key(
                                     private_key_file_object.read(),
                                     backend=default_backend(),
                                     password=None)
                    private_key_file = private_key_file_temp
                    print("\nPrivate Key file loaded.\n")

                    # load public key for private key
                    # (unload previous public key if any)
                    public_key = private_key.public_key()
                    public_key_file = None
        elif choice == '5':
            private_key_file_temp = input("\nEnter a file name for new private key: ")
            public_key_file_temp  = input("\nEnter a file name for a new public key: ")
            if os.path.exists(private_key_file_temp) or os.path.exists(public_key_file_temp):
                print("File already exists.")
            else:
                with open(private_key_file_temp, "wb+") as private_key_file_obj:
                    with open(public_key_file_temp, "wb+") as public_key_file_obj:

                        private_key = rsa.generate_private_key(
                                          public_exponent=65537,
                                          key_size=2048,
                                          backend=default_backend()
                                      )
                        public_key = private_key.public_key()

                        private_key_bytes = private_key.private_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                            encryption_algorithm=serialization.NoEncryption()
                        )
                        private_key_file_obj.write(private_key_bytes)
                        public_key_bytes = public_key.public_bytes(
                            encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo
                        )
                        public_key_file_obj.write(public_key_bytes)

                        public_key_file = None
                        private_key_file = private_key_file_temp
        elif choice == '6':
            if not (public_key or private_key):
                print("\nNo public or private key loaded\n")
            else:
                message1 = input("\nPlaintext message 1: ").encode()
                message1_as_int = bytes_to_int(message1)
                cipher1_as_int = simple_rsa_encrypt(message1_as_int, public_key)
                #cipher1 = int_to_bytes(cipher1_as_int)
                message2 = input("\nPlaintext message 2: ").encode()
                message2_as_int = bytes_to_int(message2)
                cipher2_as_int = simple_rsa_encrypt(message2_as_int, public_key)
                #cipher2 = int_to_bytes(cipher_as_int)
                multiplied = cipher1_as_int*cipher2_as_int
                multcipher = int_to_bytes(multiplied)
                cipher = binascii.unhexlify(multcipher)
                cipher_as_int = bytes_to_int(cipher)
                message_as_int = simple_rsa_decrypt(cipher_as_int, private_key)
                message = int_to_bytes(message_as_int)
                #track_recover(message.decode())
                print("\nPlaintext: {}\n".format(message))
        elif choice == '7':
            print("\n\nTerminaing. This program will self destruct in 5 seconds.\n")
            break
        else:
            print("\n\nUnknown option {}.\n".format(choice))
            
if __name__ == '__main__':
    main()
