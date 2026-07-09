from ai_search_service import (
    AISearchService
)

service = AISearchService()

results = service.search(
    "white hair maid",
    top_k=10,
)

for image in results:

    print(
        image["score"],
        image["filename"]
    )