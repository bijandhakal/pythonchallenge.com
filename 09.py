__author__ = 'bijan'
import Image,ImageDraw
from urllib2 import urlopen, HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener,install_opener
from StringIO import StringIO
from re import findall,DOTALL

URL = 'http://www.pythonchallenge.com/pc/return/good.html'
IMAGE_URL = 'http://www.pythonchallenge.com/pc/return/good.jpg'


def _auth(url):
    pass_mgr = HTTPPasswordMgrWithDefaultRealm()
    pass_mgr.add_password(None, url, 'huge', 'file')
    handelr = HTTPBasicAuthHandler(pass_mgr)
    opener = build_opener(handelr)
    install_opener(opener)
    response = urlopen(url).read()
    return response

page = _auth(URL)
first = ''.join(findall(r'first:(.*)\n\nsecond', page, DOTALL)).split(',')
first = map(lambda x: int(x), first)
second = ''.join(findall(r'second:(.*)\n\n', page, DOTALL)).split(',')
second = map(lambda x: int(x), second)
image = Image.open(StringIO(_auth(IMAGE_URL)))
draw = ImageDraw.Draw(image)
draw.line(first,'red')
draw.line(second,'red')
image.show()
