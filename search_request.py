"""
Project Athena

search_request.py

Search Request
"""

from dataclasses import dataclass

from search_type import SearchType


@dataclass
class SearchRequest:

    search_type: SearchType = SearchType.TEXT

    query: str = ""

    top_k: int = 20