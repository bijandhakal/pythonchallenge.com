__author__ = 'bijan'
from urllib2 import urlopen
from re import findall

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
NOTHING_PATTERN = r'and the next nothing is ([0-9]*)'
# next_nothing = '12345'
next_nothing = '8022'
step = 1
while next_nothing != "":
    response = urlopen(BASE_URL + next_nothing).read()
    next_nothing = ''.join(findall(NOTHING_PATTERN, response))
    print 'Step '+str(step)+": " + response
    step += 1
