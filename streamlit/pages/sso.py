import streamlit as st
import json

with open("sso.json") as f:
    sso_data = json.load(f)

st.title("SSO Accounts")

for sso in sso_data["sso"]:
    st.subheader("Sign in with {provider}".format(provider=sso["provider"]))
    for linked_account in sso["linked_accounts"]:
        st.write(linked_account)
