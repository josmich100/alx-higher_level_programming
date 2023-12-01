""" Module that posts request of letter to specific website"""
# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # posts request of letter to specific website
    URL = 'http://0.0.0.0:5000/search_user'
    try:
        q = {'q': sys.argv[1]}
        r = requests.post(URL, data=q)
        if r.headers.get('content-type') != 'application/json':
            raise TypeError
        if r.json():
            print(f"[{r.json()['id']}] {r.json()['name']}")
        else:
            print("No result")
    except IndexError:
        print("No result")
    except TypeError:
        print("Not a valid JSON")
