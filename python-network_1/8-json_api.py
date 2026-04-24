#!/usr/bin/python3
"""Sends a POST request to search_user with a given letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={'q': q})

    try:
        json_dict = response.json()
        if not json_dict:
            print("No result")
        else:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
