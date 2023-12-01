"""module that fetches a website"""
# !/usr/bin/python3
import requests


if __name__ == "__main__":
    # fetches a specific website
    URL = 'https://intranet.hbtn.io/status'
    r = requests.get(URL)
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
