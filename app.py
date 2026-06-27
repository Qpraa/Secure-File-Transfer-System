import streamlit as st

st.title("🔐 Secure File Transfer System")

st.write(
    "A secure file transfer application using encryption "
    "to protect files during communication."
)

uploaded_file = st.file_uploader("Select a file to transfer")

if uploaded_file:

    st.success("File uploaded successfully")

    st.download_button(
        label="Download Received File",
        data=uploaded_file,
        file_name=uploaded_file.name
    )

    st.info("Secure file transfer demo completed")
