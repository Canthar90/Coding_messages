import imsteg

codec = imsteg.StegCodec()

# img = codec.encode("puppy.jpg", "qualarumpull")
# img.save("puppy_x.png")  # only pngs seems to work properly.

print(codec.decode("puppy_x.png"))
