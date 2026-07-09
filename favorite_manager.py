class FavoriteManager:

    def __init__(self):

        self.favorite_images = []

    def toggle(self, image_info):

        image_id = image_info["id"]

        for img in self.favorite_images:

            if img["id"] == image_id:

                self.favorite_images = [
                    i
                    for i in self.favorite_images
                    if i["id"] != image_id
                ]

                return False

        self.favorite_images.append(
            image_info.copy()
        )

        return True

    def is_favorite(self, image_id):

        return any(
            img["id"] == image_id
            for img in self.favorite_images
        )

    def get_favorites(self):

        return self.favorite_images.copy()