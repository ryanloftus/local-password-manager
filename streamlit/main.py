import streamlit as st
import os
import os.path
import argon2
import storage
from twofish import Twofish

if not os.path.isdir(storage.PW_DIR):
    new_passcode_input = st.text_input(label="Create a passcode")
    if new_passcode_input:
        key = argon2.hash_password(new_passcode_input.encode(), hash_len=32).decode()
        t = Twofish(new_passcode_input.encode())
        accounts_file_contents = storage.encrypt(t, b'{"accounts": []}')
        sso_file_contents = storage.encrypt(t, b'{"sso": []}')
        os.mkdir(storage.PW_DIR)
        with open(storage.ACCOUNTS_FILE, "wb") as f:
            f.write(accounts_file_contents)
        with open(storage.SSO_FILE, "wb") as f:
            f.write(sso_file_contents)
        storage.key = new_passcode_input.encode()

if os.path.isdir(storage.PW_DIR):
    if storage.key is None:
        key_input = st.text_input(label="Enter your encryption key")
        if key_input:
            if storage.is_correct_key(key_input):
                storage.key = key_input.encode()
            else:
                st.error("wrong key")

    if storage.key is not None:
        st.title("Password Manager")
        st.subheader("Quick Find")
        st.text_input("Search Accounts")
