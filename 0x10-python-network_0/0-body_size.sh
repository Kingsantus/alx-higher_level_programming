#!/bin/bash
# this script that takes in a URL, sends a request to that URL and gets a response (size in bytes)
curl -s "$1" | grep "Content-Length" | cut -d ' ' -f 2
