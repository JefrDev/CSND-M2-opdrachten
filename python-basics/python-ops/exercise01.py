#!/usr/bin/env python3
"""Some description"""
import json

import requests

def perform_get(baseurl):
    """Perform get request"""
    result = requests.get(baseurl)
    print(result.content.decode())


if __name__ == "__main__":
    """Run this when called directly"""
    url = 'https://httpbin.org/get'

    perform_get(url)

