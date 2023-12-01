#!/usr/bin/python3
"""
Uses GitHub API to display the user id
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        url = 'https://api.github.com/user'

        response = requests.get(url, auth=(username, password))

        try:
            data = response.json()
            print(data.get('id'))
        except ValueError:
            print("None")
    else:
        print("Usage: ./10-my_github.py <username> <password>")
