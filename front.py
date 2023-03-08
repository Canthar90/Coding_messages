import streamlit as st
from intial_ciphering import AlphaCoder


st.set_page_config(
    layout="wide",
    page_title="Portfolio",
    page_icon="images\caesar-cipher.png"
    )

st.title("Cipher your messages within pictiures")

st.info("""
        Ciphered message will be additionally encrypted, key to you encription lies 
        in pictiure itself and code that you wil recive in popup plis copy it. 
        Send the pictiure and password to you fellow conspirator.
        """)

with st.expander("Encrypt your message"):
    raw_image =  st.file_uploader("Please choose image")
    secret_message = st.text_input("Import your secret message")
    cipher_it = st.button(label="cipher my image")
    
    
    
if raw_image and cipher_it and secret_message:
    st.text(raw_image.name)