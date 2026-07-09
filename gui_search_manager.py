from search_manager import SearchManager
from search_request import SearchRequest
from search_type import SearchType


class GuiSearchManager:

    def __init__(self):

        self.manager = SearchManager()

    def search(self, text):

        request = SearchRequest(
            search_type=SearchType.TEXT,
            query=text,
            top_k=100,
        )

        return request