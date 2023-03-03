import imsteg
import string
from random import shuffle


codec = imsteg.StegCodec()
def im_encode(text, path, out_name):
    img = codec.encode(path, text)
    img.save(out_name + ".png")  # only pngs seems to work properly.
    return "Message has ben encoded"

def im_decode(path):
    return(codec.decode(path))




options = input("Please choose option 1: Encoding \n 2: Decoding")
if options == 1: 
    text = input("Please input text to encode: ")
    path = input("Please input path to image in whitch you want your message to be encodet in: ")
    out_name =  input("Give us name of the future file")
    print(im_encode(text, path, out_name))
    
elif options == 2:
    path = input("Please provide path for image to be decoded")
    print(im_decode(path))
    
alphabet = list(string.ascii_lowercase)
coder = list(string.ascii_lowercase)
shuffle(coder)
coding_key = {}
decoding_key = {}
print(id(alphabet))
print(id(coder))
for key, val in zip(alphabet, coder):
    coding_key[key] = val
    decoding_key[val] = key
print(coding_key)
print(decoding_key)