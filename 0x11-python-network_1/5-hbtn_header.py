"""module that displays value of X-Request-Id"""
# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # displays value of variable X-Request-Id
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
