import json
from pathlib import Path


class RecentManager:

    def __init__(self, max_items=200):

        self.max_items = max_items
        self.recent_images = []

        self.data_dir = Path("data")
        self.data_dir.mkdir(
            exist_ok=True
        )

        self.file_path = (
            self.data_dir
            / "recent.json"
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

                self.recent_images = (
                    json.load(f)
                )

        except Exception:

            self.recent_images = []

    def save(self):

        try:

            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    self.recent_images,
                    f,
                    ensure_ascii=False,
                    indent=4
                )

        except Exception as e:

            print(
                "Save recent failed:",
                e
            )

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

        self.save()

    def get_recent_images(self):

        return self.recent_images.copy()

    def clear(self):

        self.recent_images.clear()

        self.save()