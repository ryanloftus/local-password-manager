import streamlit as st
import os
import os.path
import storage

if not os.path.isdir(storage.PW_DIR):
    new_passcode_input = st.text_input(label="Create a passcode")
    if new_passcode_input:
        storage.create(new_passcode_input)

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
