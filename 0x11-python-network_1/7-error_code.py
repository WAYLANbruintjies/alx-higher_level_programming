#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    err = "Error code: {}"
    status = response.status_code

    if status >= 400:
        print(err.format(status))
    else:
        print(response.text)
