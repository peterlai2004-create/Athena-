import json
from pathlib import Path


class FavoriteManager:

    def __init__(self):

        self.favorite_images = []

        self.data_dir = Path("data")
        self.data_dir.mkdir(
            exist_ok=True
        )

        self.file_path = (
            self.data_dir
            / "favorites.json"
        )

        self.load()

    def load(self):

        if not self.file_path.exists():
            return

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.favorite_images = (
                    json.load(f)
                )

        except Exception:

            self.favorite_images = []

    def save(self):

        try:

            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    self.favorite_images,
                    f,
                    ensure_ascii=False,
                    indent=4
                )

        except Exception as e:

            print(
                "Save favorites failed:",
                e
            )

    def toggle(self, image_info):

        image_id = image_info["id"]

        for img in self.favorite_images:

            if img["id"] == image_id:

                self.favorite_images = [
                    i
                    for i in self.favorite_images
                    if i["id"] != image_id
                ]

                self.save()

                return False

        self.favorite_images.append(
            image_info.copy()
        )

        self.save()

        return True

    def is_favorite(self, image_id):

        return any(
            img["id"] == image_id
            for img in self.favorite_images
        )

    def get_favorites(self):

        return self.favorite_images.copy()