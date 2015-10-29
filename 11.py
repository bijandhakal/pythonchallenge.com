__author__ = 'bijan'
from PIL import Image
from io import BytesIO
from authentication import Authentication

IMAGE_URL = 'http://www.pythonchallenge.com/pc/return/cave.jpg'

auth = Authentication(IMAGE_URL)
image = BytesIO(auth.access())
image = Image.open(image)
pix = image.load()
new_image = Image.new(image.mode,image.size)
[new_image.putpixel([i,j],pix[i,j]) for j in range(0, image.size[1], 2) for i in range(0, image.size[0], 2)]
new_image.show()
