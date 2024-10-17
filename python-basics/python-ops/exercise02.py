#!/usr/bin/env python3
"""Some description"""
import os.path

import requests


def perform_post(baseurl):
    """Perform post request"""
    inputObject = {"course": "Python Training", "name": "Exercise02"}
    headers = {'User-Agent': os.path.basename(__file__)}
    response = requests.post(baseurl, inputObject, headers=headers)
    print(response.content.decode())
    # implement this


if __name__ == "__main__":
    """Run this when called directly"""
    url = 'https://httpbin.org/post'

    perform_post(url)
