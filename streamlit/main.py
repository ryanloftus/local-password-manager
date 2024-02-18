import streamlit as st
import os
import os.path

PW_DIR = os.getenv("HOME") + "/.pw_manager"
ACCOUNTS_FILE = PW_DIR + "/accounts.json"
SSO_FILE = PW_DIR + "/sso.json"

if not os.path.isdir(PW_DIR):
    os.mkdir(PW_DIR)

if not os.path.isfile(ACCOUNTS_FILE):
    with open(ACCOUNTS_FILE, "w") as f:
        f.write('{"accounts": []}')

if not os.path.isfile(SSO_FILE):
    with open(SSO_FILE, "w") as f:
        f.write('{"sso": []}')

st.title("Password Manager")

st.subheader("Quick Find")

st.text_input("Search Accounts")
