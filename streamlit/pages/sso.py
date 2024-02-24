import streamlit as st

import storage

sso_data = storage.get_file_contents(storage.SSO_FILE)

def save_changes():
    storage.write_file_contents(storage.SSO_FILE, sso_data)

def add_new_provider(provider_name):
    for sso in sso_data["sso"]:
        if sso["provider"] == provider_name:
            # don't add duplicate provider
            return
    sso_data["sso"].append({"provider": provider_name, "linked_accounts": []})
    save_changes()

def add_new_linked_account(sso, linked_account_name):
    for account in sso["linked_accounts"]:
        if account == linked_account_name:
            # don't add duplicate linked_account
            return
    sso["linked_accounts"].append(linked_account_name)
    save_changes()

st.title("SSO Accounts")

new_sso_provider_input = st.text_input(label="New SSO Provider")
if new_sso_provider_input:
    add_new_provider(new_sso_provider_input)

for sso in sso_data["sso"]:
    st.subheader("Sign in with {provider}".format(provider=sso["provider"]))
    new_linked_account_input = st.text_input(label="New Linked Account", key="{provider}:add_linked".format(provider=sso["provider"]))
    if new_linked_account_input:
        add_new_linked_account(sso, new_linked_account_input)
    for linked_account in sso["linked_accounts"]:
        st.write(linked_account)
