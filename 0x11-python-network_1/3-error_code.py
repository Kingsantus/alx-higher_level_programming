#!/usr/bin/python3
"""Request and print response body, including error codes
"""
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except HTTPError as e:
        print(f"Error code: {e.code}")
