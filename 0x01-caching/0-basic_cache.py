#!/usr/bin/python3
"""
Import class
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Unlimited caching system
    """

    def put(self, key, item):
        """
        dictionaary
        """
        self.cache_data
        if key and item is None:
            pass

    def get(self, key):
        return self.cache_data[key]
        if key is None:
            return None
