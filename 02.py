__author__ = 'bijan'
from urllib2 import urlopen
from re import findall,DOTALL

URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = urlopen(URL).read()
comment = ''.join(findall(r'<!--\n(%.*)\n-->',response,DOTALL))
solution = ''.join(findall(r'[a-z]',comment))
print(solution)