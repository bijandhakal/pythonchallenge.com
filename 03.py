__author__ = 'bijan'
from urllib2 import urlopen
from re import findall,DOTALL

url = "http://www.pythonchallenge.com/pc/def/equality.html"
response = urlopen(url).read()
comments = "".join(findall(r'<!--\n(.*)\n-->',response,DOTALL))
solution = "".join(findall(r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}',comments))
print solution
