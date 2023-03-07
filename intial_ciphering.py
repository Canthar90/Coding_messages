import string
from random import shuffle
import random
from saver import DatabaseKelner


class AlphaCoder:
    def __init__(self, text):
        self.text =  text
        alphabet = list(string.ascii_lowercase)
        coder = list(string.ascii_lowercase)
        shuffle(coder)
        self.kelner =  DatabaseKelner()
        
        # creating encoding and decoding keys
        self.coding_key = {}
        self.decoding_key = {}
        for key, val in zip(alphabet, coder):
            self.coding_key[key] = val
            self.decoding_key[val] = key
        
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
        
    def database_input(self):
        self.kelner.save_to_db(login=self.login,
                               password=self.password,
                               key=self.decoding_key)
        
    def code_message(self):
        to_encode = list(self.text)
        new_message = ''
        for letter in to_encode:
            new_message += self.coding_key[letter]
        return new_message
        
    def decode_message(self):
        to_decode = list(self.encoded)
        new_message = ''
        for letter in to_decode:
            new_message += self.decoding_key[letter]
        return new_message
    
    
    
    
if __name__ == "__main__":
    coder = AlphaCoder("Kopytko".lower())
    print(coder.coding_key)
    print(coder.decoding_key)
    print(coder.code_message())
    print(coder.decode_message())
    coder.login_creator()
        