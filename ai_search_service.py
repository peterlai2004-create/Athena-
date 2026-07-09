from database import create_database
from feature_cache import FeatureCache
from search_manager import SearchManager
from search_request import SearchRequest
from search_type import SearchType
from image_repository import ImageRepository


class AISearchService:

    def __init__(self):

        print("=" * 50)
        print("Loading AI Search Service...")
        print("=" * 50)

        self.conn, self.cursor = create_database()

        self.cache = FeatureCache()
        self.cache.load(self.cursor)

        self.manager = SearchManager()
        self.repository = ImageRepository(
            self.cursor
        )

        print("AI Search Ready")
        print("=" * 50)

    def search(
        self,
        text,
        top_k=100,
    ):

        request = SearchRequest(
            search_type=SearchType.TEXT,
            query=text,
            top_k=top_k,
        )

        results = self.manager.search(
            self.cache,
            request,
        )

        images = []

        for result in results:

            image = self.repository.get(
                result.image_id
            )

            if image is None:
                continue

            images.append(
                {
                    "id": image.id,
                    "path": image.path,
                    "filename": image.filename,
                    "size": image.size,
                    "hash": image.hash,
                    "score": result.score,
                }
            )

        return images