"""
Project Athena

search_type.py
"""

from enum import Enum


class SearchType(Enum):

    TEXT = "text"

    IMAGE = "image"

    SIMILAR = "similar"

    HYBRID = "hybrid"