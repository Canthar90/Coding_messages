import string
from random import shuffle


class AlphaCoder:
    def __init__(self, text):
        self.text =  text
        alphabet = list(string.ascii_lowercase)
        coder = list(string.ascii_lowercase)
        shuffle(coder)
        self.coding_key = {}
        self.decoding_key = {}
        for key, val in zip(alphabet, coder):
            self.coding_key[key] = val
            self.decoding_key[val] = key
        self.encoded = self.code_message()
        
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
        