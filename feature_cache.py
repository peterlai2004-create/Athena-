"""
Project Athena

feature_cache.py

將所有 AI Feature 一次載入到記憶體。
"""

import numpy as np

from config import AI_MODEL


class FeatureCache:

    def __init__(self):

        self.image_ids = []

        self.features = None

    def load(self, cursor):

        print("=" * 50)
        print("Loading Feature Cache...")
        print("=" * 50)

        cursor.execute(
            """
            SELECT
                image_id,
                embedding

            FROM image_features

            WHERE model = ?
            """,
            (AI_MODEL,),
        )

        rows = cursor.fetchall()

        vectors = []

        self.image_ids = []

        for image_id, embedding in rows:

            vector = np.frombuffer(
                embedding,
                dtype=np.float32,
            )

            vectors.append(vector)

            self.image_ids.append(image_id)

        self.features = np.array(
            vectors,
            dtype=np.float32,
        )

        print(f"Loaded : {len(self.image_ids)}")

        print(f"Shape  : {self.features.shape}")

        print("=" * 50)