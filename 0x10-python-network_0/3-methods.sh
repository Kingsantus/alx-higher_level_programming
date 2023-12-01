#!/bin/bash
# Check if a URL is provided as a command-line argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url=$1
curl -s -i -X OPTIONS "$url" | awk '/Allow:/ {print $2}' | tr -d '\r\n'
