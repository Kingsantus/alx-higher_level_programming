#!/usr/bin/python3
""" module takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable """
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print(x_request_id)
