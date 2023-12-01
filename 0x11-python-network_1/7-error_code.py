""" Module that handles error codes"""
# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # handles error codes
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
