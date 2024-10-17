#!/usr/bin/env python3
"""Some description"""

import requests


def perform_get(baseurl):
    """Perform get request"""
    statusCode = requests.get(baseurl).status_code
    match statusCode:
        case 200:
            print("success")
        case 500:
            print("Internal Server Error")
        case _:
            print("Other status code")

    # implement this


if __name__ == "__main__":
    """Run this when called directly"""
    url1 = 'https://httpbin.org/status/200'
    url2 = 'https://httpbin.org/status/500'
    url3 = 'https://httpbin.org/status/400'

    perform_get(url1)
    perform_get(url2)
    perform_get(url3)
