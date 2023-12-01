#!/bin/bash
# Check if both URL and file are provided as command-line arguments
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi
url=$1
json_file=$2
response=$(curl -s -X POST -H "Content-Type: application/json" --data "@$json_file" "$url")

if [[ "$response" == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
