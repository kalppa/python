from PIL import Image

mac = Image.open('my_image.jpg')
print(type(mac))

# mac.show()
print(mac.filename)
print(mac.size)

""" Cropping Images """

mac.crop()