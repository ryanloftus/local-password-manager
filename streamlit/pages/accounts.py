import streamlit as st
import json

with open("accounts.json") as f:
    accounts_data = json.load(f)

st.title("Accounts")

for account in accounts_data["accounts"]:
    st.subheader(account["account"])
    for k, v in account["info"].items():
        st.write("{key}: {value}".format(key=k, value=v))
