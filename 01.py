__author__ = 'bijan'
from urllib2 import urlopen
from bs4 import BeautifulSoup
from string import maketrans,ascii_lowercase

url = 'http://www.pythonchallenge.com/pc/def/map.html'
response = urlopen(url)
soup = BeautifulSoup(response,'lxml')
text = soup.find('font', {'color':"#f000f0"}).text
# new_char = ''.join([chr((ord(char) + 2 - 97) % 26 + 97) if ord(char) in range(97, 97+26) else char for char in text])
trans = maketrans(ascii_lowercase, (ascii_lowercase[2:]+ascii_lowercase[:2]))
print str(text).translate(trans)
print 'map'.translate(trans)