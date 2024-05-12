#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    fetch = requests.get('https://alx-intranet.hbtn.io/status')
    txt = fetch.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(txt), txt))
