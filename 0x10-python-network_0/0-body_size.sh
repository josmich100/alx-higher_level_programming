#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response in bytes

url=$1
curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}'
