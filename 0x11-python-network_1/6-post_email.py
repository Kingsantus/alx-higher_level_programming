#!/usr/bin/python3
"""Make a POST request
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url, email = argv[1], argv[2]

    email_data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=email_data) as response:
        body = response.read().decode('utf-8')
        print(body)

