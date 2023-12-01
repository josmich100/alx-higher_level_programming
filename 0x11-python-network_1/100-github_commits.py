#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a GitHub repository by a user
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        owner = sys.argv[2]
        repo = sys.argv[1]

        url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        params = {'per_page': 10}

        response = requests.get(url, params=params)

        try:
            commits = response.json()
            for commit in commits:
                sha = commit.get('sha')
                author_name = commit.get('commit', {}).get('author', {}).get('name')
                print(f"{sha}: {author_name}")

        except ValueError:
            print("Not a valid JSON")

    else:
        print("Usage: ./100-github_commits.py <repo_name> <owner_name>")
