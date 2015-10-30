__author__ = 'bijan'
import xmlrpclib

URL = 'http://www.pythonchallenge.com/pc/phonebook.php'

serverproxy = xmlrpclib.ServerProxy(URL)
# print serverproxy.system.listMethods()
# print serverproxy.system.methodSignature('phone')
# print serverproxy.system.methodHelp('phone')
print serverproxy.phone('Bert')
