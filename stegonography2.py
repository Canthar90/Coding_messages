# import imsteg
from PIL import Image
from pathlib import Path
from typing import Union, Generator

import numpy as np
from PIL import Image


class StegCodec:
    def _flatten(
        self,
        data,
        text_data: list[str]
    ) -> Generator[np.ndarray, None, None]:
        for i in range(len(text_data)):
            pixels = np.array(next(data)[:3] + next(data)[:3] + next(data)[:3])
            bit_array = np.array([*map(int, text_data[i] + "0")])
            res = np.abs(pixels - ((pixels % 2) ^ bit_array))
            yield from res.reshape(3, 3)

    def encode(
        self,
        image: Union[str, bytes, Path],
        text: str
    ) -> Image.Image:
        """Encodes the text to the image.

        Parameters
        ----------
        image: Union[str, bytes, Path, SupportsRead[bytes]]
            The image to encode.
        text: :class:`str`
            The text to encode to the image.

        Returns
        ----------
        :class:`PIL.Image.Image`
            The encoded image object.
        """

        text_data = [f"{ord(i):08b}" for i in text]

        with Image.open(image) as img:  # type: ignore
            new_image = img.copy()
            data = iter(img.getdata())

        if len(text_data) > len(list(new_image.getdata())) // 3:
            raise ValueError("The image is too small for the text!")

        img_width, _ = new_image.size
        x, y = 0, 0

        for pixels in self._flatten(data, text_data):
            new_image.putpixel((x, y), tuple(pixels))  # type: ignore

            if x == img_width - 1:
                x = 0
                y += 1
            else:
                x += 1

        if pixels[-1] % 2 == 0:
            if pixels[-1] != 0:
                pixels[-1] -= 1
            else:
                pixels[-1] += 1

        new_image.putpixel((x-1, y), tuple(pixels))  # type: ignore

        return new_image

    def decode(
        self,
        data, iter_data
    ) -> str:
        """Decodes an image.

        Parameters
        ----------
        image: Union[str, bytes, Path, SupportsRead[bytes]]

        Returns
        :class:`str`
            The decoded text.
        """

        # with Image.open(image) as img:  # type: ignore
            # data = img.getdata()
            # iter_data = iter(data)
        # data = image.getdata()
        # iter_data = iter(data)

        if len(data) < 3:
            raise ValueError("Image is too small!")

        text = ""

        while True:
            flattened = np.array(
                next(iter_data)[:3]
                + next(iter_data)[:3]
                + next(iter_data)[:3]
            )

            bin_txt = ""

            for pix in flattened[:8]:
                if pix % 2 == 0:
                    bin_txt += "0"
                else:
                    bin_txt += "1"

            text += chr(int(bin_txt, 2))

            if flattened[-1] % 2 != 0:
                return text




class SeganographCoder():
    
    def __init__(self):
        self.codec = StegCodec()
    
    def im_encode(self, text, path, out_name):
        img = self.codec.encode(path, text)
        img.save(out_name + ".png") 
        img_name = out_name + ".png"
        return img, img_name

    def im_decode(self, data ,iter_data):
        res = (self.codec.decode(data ,iter_data))
        print(res)
        return res



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
        
