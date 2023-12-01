#!/bin/bash

# Check if a URL is provided as a command-line argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email&subject=$subject" "$url" | grep -A2 "POST params:"
