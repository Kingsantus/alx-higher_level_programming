#!/bin/bash
# Check if a URL is provided as a command-line argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
url=$1
curl -s -H "X-School-User-Id: 98" "$url"
