#!/bin/bash
# this script that takes in a URL, sends a request to that URL and gets a response (size in bytes)
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url=$1
curl -s "$url" | wc -c
