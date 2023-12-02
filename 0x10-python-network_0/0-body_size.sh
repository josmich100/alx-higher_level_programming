#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response in bytes

url=$1
curl -s "$url" | wc -c
