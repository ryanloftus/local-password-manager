import streamlit as st
import json
import pyperclip

with open("accounts.json") as f:
    accounts_data = json.load(f)

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

for account in accounts_data["accounts"]:
    st.subheader(account["account"])
    col1, col2, col3 = st.columns([1,3,1])
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

