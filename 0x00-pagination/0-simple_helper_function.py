#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 2023 12:00:00

@Author: Nicanor Kyamba
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns start and end index for pagination

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
