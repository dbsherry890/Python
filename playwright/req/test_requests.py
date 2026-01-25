import requests
from requests.exceptions import HTTPError
import json


def test_error_handling():
    try:
        response = requests.get("https://api.github.com/")
        response.raise_for_status()  # raises HTTPError for codes 4-600
    except HTTPError as e:
        print(e)
    else:
        data = response.json()
        print(json.dumps(data, indent=4, sort_keys=True))  # viewable format


def test_post():
    response = requests.post("https://httpbin.org/post", json={"name": "Dan"})
    json_response = response.json()
    print(json_response["data"])
    print(json_response["headers"]["Content-Type"])


def test_response_request():
    response = requests.get("https://api.github.com/")
    print(response.request.url)
    response.request.path_url


if __name__ == "__main__":
    test_response_request()
