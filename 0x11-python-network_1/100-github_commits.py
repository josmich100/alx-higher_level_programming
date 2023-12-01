"""user Github API to list 10 commits from specific user in specific REPO"""
# !/usr/bin/python3
import sys
import requests


if __name__ == "__main__":
    # user Github API to list 10 commits from specific user in specific REPO
    try:
        REPO = sys.argv[1]
        OWNER = sys.argv[2]
        URL = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'
        r = requests.get(URL)
        r_json = r.json()
        LENGTH = len(r_json)
        if LENGTH == min(LENGTH, 10):
            for i in range(LENGTH):
                print(f"{r_json[i].get('sha')}: {r_json[i].get('commit').get('author').get('name')}")
    except:
        print("None")
