__author__ = 'bijan'
import Image
from urllib2 import urlopen
from StringIO import StringIO

URL = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
response = urlopen(URL).read()
image = Image.open(StringIO(response))

pix = image.load()
rbga = [pix[i,43] for i in range(0, image.size[0], 7)]
message = ''.join([chr(rbg[0]) for rbg in rbga if rbg[0] == rbg[1] == rbg[2]])
print message

li = [105, 110, 116, 101, 103, 114, 105, 116, 121]
final_message = ''.join([chr(i) for i in li])
print final_message
