import streamlit as st
from cryptography.fernet import Fernet

st.title("Secure File Transfer System")

st.write("AES Encryption based secure file transfer demo")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    key = Fernet.generate_key()
    cipher = Fernet(key)

    encrypted_file = cipher.encrypt(uploaded_file.read())

    st.success("File encrypted successfully")

    st.download_button(
        "Download Encrypted File",
        encrypted_file,
        file_name="encrypted_file.txt"
    )

    st.info("Keep this key safe:")
    st.code(key.decode())
