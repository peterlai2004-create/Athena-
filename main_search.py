"""
Project Athena

AI Search
"""

from database import create_database
from feature_cache import FeatureCache
from search_manager import SearchManager
from search_request import SearchRequest
from search_type import SearchType
from image_repository import ImageRepository

conn, cursor = create_database()

cache = FeatureCache()
cache.load(cursor)

manager = SearchManager()
repository = ImageRepository(cursor)

request = SearchRequest(
    search_type=SearchType.TEXT,
    query="white hair maid",
)

results = manager.search(
    cache,
    request,
)

print()
print("=" * 60)

for result in results:

    image = repository.get(result.image_id)

    if image is None:
        continue

    print(f"{result.score:.4f}")
    print(image.path)
    print()

print("=" * 60)

conn.close()