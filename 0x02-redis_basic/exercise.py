#!/usr/bin/env python3
""" Script for Writing basic redis commands with python """
from typing import Any
from uuid import uuid4
import redis


class Cache(object):
    """docstring for Cache"""
    def __init__(self):
        """ Method for initiating the class instance """
        self._redis = redis.Redis()
        self.flushdb = self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ A method for storing a key value pair in the redis server """
        key = uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn=None) -> str:
        """ A method for reteriving the value associated with the key """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
