#!/bin/bash
# This script takes a URL, sends a GET request and display the body of a 200 status code response
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url=$1
curl -s -o /dev/null -w "%{http_code}" "$url" | {
    read -r status
    if [ "$status" = "200" ]; then
        curl -s "$url"
    fi
}
