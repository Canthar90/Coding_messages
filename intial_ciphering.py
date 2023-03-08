import string
from random import shuffle
import random
from saver import DatabaseKelner, Hasher
from stegonography2 import SeganographCoder


class AlphaCoder:
    def __init__(self, text):
        self.text =  text.lower()
        alphabet = list(string.ascii_lowercase + string.digits + string.punctuation +" ")
        coder = list(string.ascii_lowercase + string.digits + string.punctuation + " ")
        shuffle(coder)
        
        # Creating class instances
        self.kelner =  DatabaseKelner()
        self.hasher = Hasher()
        self.steg = SeganographCoder()
        
        # creating encoding and decoding keys
        self.coding_key = {}
        self.decoding_key = {}
        for key, val in zip(alphabet, coder):
            self.coding_key[key] = val
            self.decoding_key[val] = key
            
        print(f"coding key is  {self.coding_key}" )
        
        self.encoded = self.code_message()
        self.login = '' 
        self.login_creator()
        self.password = ''
        self.password_creator()
    
    def login_creator(self):
        free_login = False
        while not free_login:
            characters = string.ascii_letters + string.digits + string.punctuation
            login = ''.join(random.choice(characters) for i in range(10))
            free_login = self.kelner.check_if_login_is_free(login)
        message_bufor =  login
        self.login = login
        print(login)
        self.encoded = message_bufor + "___"+ self.encoded
        print(self.encoded)
         
    def password_creator(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.choice(characters) for i in range(10))
        self.hasher.hash_it(self.password)
        
    def database_input(self):
        self.kelner.save_to_db(login=self.login,
                               password=self.password,
                               key=self.decoding_key)
        
    def database_out(self, login, passowrd):
        return self.kelner.retrive_key(login=login, password=passowrd)
        
        
    def code_message(self):
        to_encode = list(self.text)
        new_message = ''
        for letter in to_encode:
            new_message += self.coding_key[letter]
        return new_message
        
    def decode_message(self, decode_key, message):
        to_decode = list(message)
        new_message = ''
        for letter in to_decode:
            new_message += decode_key[letter]
        return new_message
    
    def code_to_img(self, img, out_name):
        coded_img, im_name = self.steg.im_encode(text=self.encoded, path=img,
                                        out_name=out_name)
        self.database_input()
        return coded_img, im_name, self.password
    
    def img_decode(self, img):
        message = self.steg.im_decode(img)
        return message
    
    def decode_message(self, img, password):
        decoded = self.img_decode(img)
        print(f"first {decoded}")
        login = decoded.split("___")[0]
        print(f"second {decoded}")
        encoded_message = decoded.split("___")[1]
        decode_key = self.database_out(login=login, passowrd=password)
        message = self.decode_message(decode_key, encoded_message)
        return message
        
        
        
        
    
    
    
    
if __name__ == "__main__":
    coder = AlphaCoder("Kopytko".lower())
    print(coder.coding_key)
    print(coder.decoding_key)
    print(coder.code_message())
    print(coder.decode_message())
    
        