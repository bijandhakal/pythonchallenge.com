__author__ = 'bijan'
import Image,ImageDraw
from StringIO import StringIO
from re import findall,DOTALL
from authentication import Authentication

URL = 'http://www.pythonchallenge.com/pc/return/good.html'
IMAGE_URL = 'http://www.pythonchallenge.com/pc/return/good.jpg'

page = Authentication(URL,'huge','file').access()
first = ''.join(findall(r'first:(.*?)\n\n', page, DOTALL)).split(',')
first = map(lambda x: int(x), first)
second = ''.join(findall(r'second:(.*?)\n\n', page, DOTALL)).split(',')
second = map(lambda x: int(x), second)
image = Image.open(StringIO(Authentication(IMAGE_URL,'huge','file').access()))
new_image = Image.new(image.mode,image.size,color='#FFFFFF')
draw = ImageDraw.Draw(new_image)
draw.line(first,'red')
draw.line(second,'red')
new_image.show()
