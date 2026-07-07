"""
Project Athena

search_result.py

Search Result
"""

from dataclasses import dataclass


@dataclass
class SearchResult:
    image_id: int
    score: float