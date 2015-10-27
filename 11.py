__author__ = 'bijan'
import Image
from urllib2 import urlopen,HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener,install_opener
from StringIO import StringIO

IMAGE_URL = 'http://www.pythonchallenge.com/pc/return/cave.jpg'


def _auth(url):
    ps_mgr = HTTPPasswordMgrWithDefaultRealm()
    ps_mgr.add_password(None, url, 'huge', 'file')
    handler = HTTPBasicAuthHandler(ps_mgr)
    opener = build_opener(handler)
    install_opener(opener)
    response = urlopen(url).read()
    return response


image = StringIO(_auth(IMAGE_URL))
image = Image.open(image)
pix = image.load()
new_image = Image.new(image.mode,image.size)
[new_image.putpixel([i,j],pix[i,j]) for j in range(0, image.size[1], 2) for i in range(0, image.size[0], 2)]
new_image.show()
