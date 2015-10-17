__author__ = 'bijan'
from urllib2 import urlopen
from zipfile import ZipFile
from StringIO import StringIO
from re import findall

URL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
NOTHING_PATTERN = r'[0-9]*'

response = urlopen(URL).read()
zip_data = ZipFile(StringIO(response), 'r')
content = zip_data.read('90052.txt')
comment = zip_data.getinfo('90052.txt').comment
while content:
    try:
        next_nothing = ''.join(findall(NOTHING_PATTERN,content))
        next_file = str(next_nothing)+'.txt'
        content = zip_data.read(next_file)
        comment += zip_data.getinfo(next_file).comment
    except KeyError:
        content = None
print comment

