__author__ = 'bijan'
from urllib2 import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, install_opener, urlopen


class Authentication:
    def __init__(self,link,username,password):
        self.url = link
        ps_mgr = HTTPPasswordMgrWithDefaultRealm()
        ps_mgr.add_password(None, self.url, username, password)
        handler = HTTPBasicAuthHandler(ps_mgr)
        opener = build_opener(handler)
        install_opener(opener)

    def access(self):
        response = urlopen(self.url).read()
        return response
