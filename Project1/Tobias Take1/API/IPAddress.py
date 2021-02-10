import socket
from unittest.mock import patch
import requests
import re

orig_getaddrinfo = socket.getaddrinfo

def getaddrinfoIPv6(host, port, family=0, type=0, proto=0, flags=0):
    return orig_getaddrinfo(host=host, port=port, family=socket.AF_INET6, type=type, proto=proto, flags=flags)

def getaddrinfoIPv4(host, port, family=0, type=0, proto=0, flags=0):
    return orig_getaddrinfo(host=host, port=port, family=socket.AF_INET, type=type, proto=proto, flags=flags)

def getMyIPv4Address():
    with patch('socket.getaddrinfo', side_effect=getaddrinfoIPv4):
        r = requests.get('http://ip6.me')
        address = re.search(r'\+3>(.*?)</',r.content.decode('utf-8')).group(1)
        print('IPv4: ' + address)
        return address
    
def getMyIPv6Address():
   with patch('socket.getaddrinfo', side_effect=getaddrinfoIPv6):
       r = requests.get('http://ip6.me')
       address = re.search(r'\+3>(.*?)</',r.content.decode('utf-8')).group(1)
       print('IPv6: ' + address)
       return address

