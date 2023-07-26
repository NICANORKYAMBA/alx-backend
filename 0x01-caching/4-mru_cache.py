#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
"""
Created on Wed 26 July 10:00:00 2023

@Author Nicanor Kyamba
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item to the cache

        Args:
            key (str): key
            item (str): item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)
            else:
                self.queue.append(
                        self.queue.pop(self.queue.index(key)))
            if len(self.queue) > BaseCaching.MAX_ITEMS:
                removed = self.queue.pop(-2)
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

    def get(self, key):
        """
        Retrieves an item from the cache

        Args:
            key (str): key
        """
        if key is None or key not in self.cache_data:
            return None
        self.queue.append(self.queue.pop(self.queue.index(key)))
        return self.cache_data[key]
