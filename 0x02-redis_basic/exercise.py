#!/usr/bin/env python3
""" Script for Writing basic redis commands with python """
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable


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


def call_history(method: Callable) -> Callable:
    """ Function for storing the history of inputs and outputs of a
        function
        Args:
            :params: method[Callable] - A callable function
        Return:
            This function returns a callable
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
        self._redis.rpush("{}:inputs".format(key), str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(key), output)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable) -> None:
    """ Function that displays thehistory of calss of a particular function
        Args:
            :params: method[Callable] - A callable function
        Return:
            This function returns no variable
    """
    cache, key = redis.Redis(), method.__qualname__
    num = int(cache.get(key))
    time = "times" if int(num) > 1 else "time"
    print("{} was called {} {}:".format(key, num, time))
    inputs = cache.lrange("{}:inputs".format(key), 0, -1)
    outputs = cache.lrange("{}:outputs".format(key), 0, -1)
    for name, value in zip(inputs, outputs):
        name, value = name.decode('utf-8'), value.decode('utf-8')
        print("{}(*{}) -> {}".format(key, name, value))


class Cache(object):
    """docstring for Cache"""
    def __init__(self):
        """ Method for initiating the class instance """
        self._redis = redis.Redis()
        self.flushdb = self._redis.flushdb()

    @call_history
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
