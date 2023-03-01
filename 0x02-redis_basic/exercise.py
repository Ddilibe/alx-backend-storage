#!/usr/bin/env python3
""" Script for Writing basic redis commands with python """
from typing import Any, Callable
from functools import wraps
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """ Method for counting the number of times a call was made
        Args:
            :params: fun[Callable] - A function to be called
        Return:
            This function returns a function to be called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """ Function for the actual counting
            Args:
                :params: args[List] - List of probable parameters
                :params: kwargs[Dict] - Dict of probable parameters
            Return: Returns a callable
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache(object):
    """docstring for Cache"""
    def __init__(self):
        """ Method for initiating the class instance """
        self._redis = redis.Redis()
        self.flushdb = self._redis.flushdb()

    @count_calls
    def store(self, data: Any) -> str:
        """ A method for storing a key value pair in the redis server """
        key = uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn=None) -> Any:
        """ A method for reteriving the value associated with the key """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
