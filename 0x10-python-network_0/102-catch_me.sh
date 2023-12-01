#!/bin/bash

# Use curl to make a request that triggers the server response
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
