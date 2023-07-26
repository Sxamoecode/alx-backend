#!/usr/bin/python3
"""Caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Import dict from parent class
    """

    def put(self, key, item):
        """
        assign item to caching system
        """
        if key is None or item is None:
            return
        self.caching_data[key] = item

    def get(self, key):
        """
        return value in cache
        """
        return self.cache_data.get(key, None)
