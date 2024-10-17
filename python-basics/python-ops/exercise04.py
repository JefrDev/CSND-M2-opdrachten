#!/usr/bin/env python3
"""Some description"""
import json

import requests


def perform_get(baseurl):
    """Perform get request"""

    req = requests.get(baseurl)
    parse_data(req.json())


def parse_data(data):
    title = data["slideshow"]["title"]
    author = data["slideshow"]["author"]
    date = data["slideshow"]["date"]
    slides = data["slideshow"]["slides"]

    print(f"the title is: {title}")
    print(f"the author is: {author}")
    print(f"it was published on: {date}")
    print("it contains the following slides:")
    for i in range(len(slides)):
        print(f"- {slides[i]["title"]}")
    """Parse the returned data"""



if __name__ == "__main__":
    """Run this when called directly"""
    url = 'https://httpbin.org/json'

    perform_get(url)
