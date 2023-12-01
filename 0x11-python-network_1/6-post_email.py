#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        # Data to be sent in the POST request
        data = {'email': email}

        response = requests.post(url, data=data)
        print(response.text)
    else:
        print("Usage: ./6-post_email.py <URL> <email>")
