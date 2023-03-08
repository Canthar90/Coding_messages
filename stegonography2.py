import imsteg
from PIL import Image


class SeganographCoder():
    
    def __init__(self):
        self.codec = imsteg.StegCodec()
    
    def im_encode(self, text, path, out_name):
        img = self.codec.encode(path, text)
        img.save(out_name + ".png") 
        img_name = out_name + ".png"
        return img, img_name

    def im_decode(self, path):
        return(self.codec.decode(path))



if __name__ == "__main__":
    codec = SeganographCoder()
    options = input("Please choose option 1: Encoding \n 2: Decoding: ")
    if options == "1": 
        text = input("Please input text to encode: ")
        path = input("Please input path to image in whitch you want your message to be encodet in: ")
        out_name =  input("Give us name of the future file: ")
        
        image = Image.open("puppy.jpg")
        print(codec.im_encode(text, image, out_name))
        
    elif options == 2:
        path = input("Please provide path for image to be decoded")
        print(codec.im_decode(path))
        
