#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if the status code is 200

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    curl -s "$url"
fi
