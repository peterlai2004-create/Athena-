class RecentManager:

    def __init__(self, max_items=200):

        self.max_items = max_items
        self.recent_images = []

    def add(self, image_info):

        image_id = image_info["id"]

        self.recent_images = [
            img
            for img in self.recent_images
            if img["id"] != image_id
        ]

        self.recent_images.insert(
            0,
            image_info.copy()
        )

        self.recent_images = (
            self.recent_images[:self.max_items]
        )

    def get_recent_images(self):

        return self.recent_images.copy()

    def clear(self):

        self.recent_images.clear()