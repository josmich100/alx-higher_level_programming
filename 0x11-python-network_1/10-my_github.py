"""script that takes your GitHub credentials to display your id"""
# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # uses Github credentials to display ID
    try:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]
        URL = 'https://api.github.com/user'
        r = requests.get(URL, auth=(USERNAME, PASSWORD))
        json_r = r.json()
        print(json_r.get('id'))
    except:
        print("None")
