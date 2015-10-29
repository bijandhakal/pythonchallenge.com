__author__ = 'bijan'
import Image,ImageDraw
from StringIO import StringIO
from re import findall,DOTALL
from authentication import Authentication

URL = 'http://www.pythonchallenge.com/pc/return/good.html'
IMAGE_URL = 'http://www.pythonchallenge.com/pc/return/good.jpg'

page = Authentication(URL,'huge','file').access()
first = ''.join(findall(r'first:(.*)\n\nsecond', page, DOTALL)).split(',')
first = map(lambda x: int(x), first)
second = ''.join(findall(r'second:(.*)\n\n', page, DOTALL)).split(',')
second = map(lambda x: int(x), second)
image = Image.open(StringIO(Authentication(URL,'huge','file').access()))
draw = ImageDraw.Draw(image)
draw.line(first,'red')
draw.line(second,'red')
image.show()
