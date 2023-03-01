#!/usr/bin/env python3
""" Script that test redis with requests to external sources """
import redis
import requests

cache, count = redis.Redis(), 0


def get_page(url: str) -> str:
    """ Get a page and cache a value """
    req, param = request.get(url), "cached: {}".format(url)
    cache.set(param, count)
    cache.incr(param)
    cache.setex(param, 10, cache.get(param))
    return req.text


if __name__ == '__main__':
    get_page("http://slowwly.robertomurray.co.uk")
