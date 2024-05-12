#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    u_name = argv[1]
    p_word = argv[2]
    auth = HTTPBasicAuth(u_name, p_word)

    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
