__author__ = 'bijan'
from urllib2 import urlopen
import pickle

URL = 'http://www.pythonchallenge.com/pc/def/banner.p'
response = urlopen(URL).read()
data = pickle.loads(response)

for line in data:
    out = ''.join([el[0] * el[1] for el in line])
    print(out)
