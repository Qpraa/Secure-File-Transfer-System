!pip install streamlit cryptography
import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(
    page_title="Secure File Transfer System",
    page_icon="🔐"
)

st.title("🔐 Secure File Transfer System")

st.write(
    "A secure file transfer application using AES-256 encryption "
    "to protect files from unauthorized access."
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:

    key = Fernet.generate_key()

    cipher = Fernet(key)

    data = uploaded_file.read()

    encrypted_data = cipher.encrypt(data)

    st.success("File encrypted successfully!")

    st.download_button(
        label="Download Encrypted File",
        data=encrypted_data,
        file_name="encrypted_file.txt"
    )

    st.warning("Save this encryption key:")
    st.code(key.decode())    
