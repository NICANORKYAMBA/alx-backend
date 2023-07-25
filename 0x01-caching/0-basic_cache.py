#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
"""
Created on Tue July 25 13:00:00 2023

@Author: Nicanor Kyamba
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def put(self, key, item):
        """
        Adds an item to the cache

        Args:
            key (str): key
            item (str): item
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache

        Args:
            key (str): key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
