# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # posts an email
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=email)
    print(r.text)
