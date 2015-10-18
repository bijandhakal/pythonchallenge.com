__author__ = 'bijan'
from urllib2 import urlopen
from bz2 import decompress
from re import findall

URL = 'http://www.pythonchallenge.com/pc/def/integrity.html'
response = urlopen(URL).read()
un = findall(r'un: \'(.*)\'',response)[0].decode('string_escape')
pw = findall(r'pw: \'(.*)\'',response)[0].decode('string_escape')
un = decompress(un)
pw = decompress(pw)
print un, pw

