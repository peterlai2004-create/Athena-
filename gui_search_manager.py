from search_request import SearchRequest
from search_type import SearchType


class GuiSearchManager:

    def __init__(self):

        pass

    def search(self, text):

        text = text.strip()

        if text.startswith("ai:"):

            query = text[3:].strip()

            return SearchRequest(
                search_type=SearchType.TEXT,
                query=query,
                top_k=100,
            )

        return SearchRequest(
            search_type=SearchType.HYBRID,
            query=text,
            top_k=100,
        )