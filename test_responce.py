# coding=utf-8
import requests
import datetime


def test_connection(url):
    resp = requests.get(url)
    return resp.status_code


if __name__ == "__main__":
    print("Test started")

    while True:
        r = test_connection("http://swarm-example.loc/")
        print(r)
        # if r == 404:
        #     print("old", datetime.datetime.now())
        # elif r == 502 or r == 503:
        #     print("error", datetime.datetime.now())
        # elif r == 500:
        #     print("new", datetime.datetime.now())

