import os
import json
from twofish import Twofish

PW_DIR = os.getenv("HOME") + "/.pw_manager"
ACCOUNTS_FILE = PW_DIR + "/accounts.json"
SSO_FILE = PW_DIR + "/sso.json"

key: bytes = None

BLOCK_SIZE = 16

def encrypt(t: Twofish, plaintext: bytes):
    while len(plaintext) % BLOCK_SIZE != 0:
        plaintext += b' '
    ciphertext = ''.encode()
    while len(plaintext) > 0:
        next_block = plaintext[:BLOCK_SIZE]
        plaintext = plaintext[BLOCK_SIZE:]
        ciphertext += t.encrypt(next_block)
    return ciphertext

def decrypt(t: Twofish, ciphertext: bytes):
    plaintext = ''.encode()
    while len(ciphertext) > 0:
        next_block = ciphertext[:BLOCK_SIZE]
        ciphertext = ciphertext[BLOCK_SIZE:]
        plaintext += t.decrypt(next_block)
    return plaintext.decode().strip()

def get_file_contents(file):
    with open(file, "rb") as f:
        file_contents = f.read()
    t = Twofish(key)
    return json.loads(decrypt(t, file_contents))

def write_file_contents(file, data):
    t = Twofish(key)
    file_contents = json.dumps(data)
    encrypted_file_contents = encrypt(t, file_contents.encode())
    with open(file, "wb") as f:
        f.write(encrypted_file_contents)

def is_correct_key(key: str):
    return True
