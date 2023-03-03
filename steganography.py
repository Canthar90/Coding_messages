import cv2
import numpy as np
import types


def to_bin(message: str):
    if isinstance(message, str):
        return ''.join([format(ord(i), "08b")for i in message])
    else:
        return False


message = input("Please provide message to be encoded :")
binary_encoded = to_bin(message)
print(binary_encoded) if binary_encoded else print("Sory your input is invalid")
    
