import streamlit as st
from intial_ciphering import AlphaCoder
from io import BytesIO
from PIL import Image



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
        Special characters like ?!<> etc will be lost in message.
        """)

with st.expander("Encrypt your message"):
    raw_image =  st.file_uploader("Please choose image")
    secret_message = st.text_input("Import your secret message")
    cipher_it = st.button(label="Cipher my image")
 
    
with st.expander("Decrypt your message"):
    encrypted_image = st.file_uploader("Please choose encrypted image")
    secret_password = st.text_input("Input image secret password")
    decrypt_it = st.button(label="Decrypt")
    
    
# Ciphering message in the pictiure 
if raw_image and cipher_it and secret_message and (".jpg" in raw_image.name or ".png" in raw_image.name ):
    buf = BytesIO()
    coder = AlphaCoder(secret_message)
    new_name = "crypted" 
    coded_image, image_name, password =coder.code_to_img(img=raw_image, out_name=new_name)
    coded_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    coded_one = st.image(coded_image, caption="This is image with coded message save it")
    with open("crypted.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="encrypted.jpg",
            mime="image/png",
            )
    
    st.success(f'Your decrypting password: {password}', icon="✅")
    
    
# Decrypting message 
if decrypt_it and encrypted_image and (".jpg" in encrypted_image.name  or ".png" in encrypted_image.name):
    with open("encrypted.png", "wb") as file:
        imagge = file.write(encrypted_image.getbuffer())
    coder = AlphaCoder("init")
    with Image.open("encrypted.png") as img:  # type: ignore
        data = img.getdata()
        iter_data = iter(data)
    
    decrypted_msg =  coder.decode_message_final(data=data, iter_data=iter_data, password=secret_password)
    st.subheader("Your secret message will be displayed below")
    st.text(decrypted_msg)
    

