"""
Project Athena

Search Manager
"""

from search_engine import search as feature_search
from search_request import SearchRequest
from search_type import SearchType
from request_analyzer import RequestAnalyzer


class SearchManager:

    def __init__(self):

        self.analyzer = RequestAnalyzer()

    def search(
        self,
        cache,
        request: SearchRequest,
    ):

        concepts = self.analyzer.analyze(request.query)

        character = []
        feature = []
        purpose = []
        unknown = []

        for token in concepts:

            if token.concept == "character":
                character.append(token.word)

            elif token.concept == "feature":
                feature.append(token.word)

            elif token.concept == "purpose":
                purpose.append(token.word)

            else:
                unknown.append(token.word)

        print("\n========== Search Analysis ==========")
        print("Character :", character)
        print("Feature   :", feature)
        print("Purpose   :", purpose)
        print("Unknown   :", unknown)
        print("=====================================\n")

        # 暫時還是走原本 Feature Search
        return feature_search(
            cache=cache,
            text=request.query,
            top_k=request.top_k,
        )