import streamlit as st
import pyperclip
import storage

accounts_data = storage.get_file_contents(storage.ACCOUNTS_FILE)

def save_changes():
    storage.write_file_contents(storage.ACCOUNTS_FILE, accounts_data)

def add_new_account(account_name):
    for account in accounts_data["accounts"]:
        if account["account"] == account_name:
            # don't add duplicate account
            return
    accounts_data["accounts"].append({"account": account_name, "info": {}})
    save_changes()

def get_key_input_id(account):
    return "{acct}:keyinput".format(acct=account["account"])

def get_value_input_id(account):
    return "{acct}:valinput".format(acct=account["account"])

def add_new_account_info(account, key, value):
    st.session_state[get_key_input_id(account)] = ""
    st.session_state[get_value_input_id(account)] = ""
    account["info"][key] = value
    save_changes()

st.title("Accounts")

# center the button and text elements vertically within each "row" so that "Copy" button is aligned with corresponding text
st.write(
    """<style>
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

new_account_input = st.text_input(label="New Account", key="newacct")
if new_account_input:
    add_new_account(new_account_input)

for account in accounts_data["accounts"]:
    st.subheader(account["account"])
    col1, col2, col3 = st.columns([1,3,1])
    with col1:
        new_account_info_key_input = st.text_input(
            label="New Account Info Key",
            key=get_key_input_id(account),
            label_visibility="collapsed",
        )
    with col2:
        new_account_info_value_input = st.text_input(
            label="New Account Info Value",
            key=get_value_input_id(account),
            label_visibility="collapsed",
        )
    with col3:
        add_new_account_info_button = st.button(
            label="Add",
            key="{acct}:addbtn".format(acct=account["account"]),
            on_click=lambda a=account, k=new_account_info_key_input, v=new_account_info_value_input: add_new_account_info(a, k, v),
        )
    for k, v in account["info"].items():
        with col1:
            st.markdown("**{key}**:".format(key=k))
        with col2:
            st.markdown("`{value}`".format(value=v))
        with col3:
            st.button(
                label="Copy",
                key="{acct}:{attr}".format(acct=account["account"], attr=k),
                on_click=lambda content=v: pyperclip.copy(content),
            )

