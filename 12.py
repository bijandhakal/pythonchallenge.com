__author__ = 'bijan'
from PIL import Image
from io import BytesIO
from authentication import Authentication
import os

GFX_URL = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
auth = Authentication(GFX_URL, 'huge', 'file')
gfx_read = auth.access()

if not os.path.exists('/12solution'):
    os.makedirs('12solution')

for i in range(5):
    image = gfx_read[i::5]
    image_object = Image.open(BytesIO(image))
    with open("12solution/%d.%s" % (i, image_object.format.lower()), "wb") as imagefile:
        imagefile.write(image)

