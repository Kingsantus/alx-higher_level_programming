#!/usr/bin/python3
"""  script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) """
import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}

    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')

    # make request object
    request = urllib.request.Request(url, email)

    with urllib.request.urlopen(request) as response:
        response = response.read()
        response = response.decode('utf-8')
        print(response)
