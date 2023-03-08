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
    coder = AlphaCoder(secret_message)
    new_name = "crypted" 
    coded_image, image_name, password =coder.code_to_img(img=raw_image, out_name=new_name)
    coded_one = st.image(coded_image, caption="This is image with coded message save it")
    
    st.success(f'Your decrypting password: {password}', icon="✅")
    
    
    
    
    # st.text("checking if it works")
    # st.text(coded_image.__str__)
    # decoded_raw_msg = coder.img_decode(image_name)
    
    # st.text(decoded_raw_msg)
    