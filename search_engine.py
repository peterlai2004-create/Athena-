"""
Project Athena

search_engine.py

AI Text Search
"""

import numpy as np
import open_clip
import torch

from search_result import SearchResult

# ==================================================
# Device
# ==================================================

device = "cuda" if torch.cuda.is_available() else "cpu"

print("=" * 50)
print("Loading Text Encoder...")

# ==================================================
# Load Model
# ==================================================

model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms(
    "ViT-B-32",
    pretrained="laion2b_s34b_b79k",
)

tokenizer = open_clip.get_tokenizer("ViT-B-32")

model = model.to(device)
model.eval()

print("Text Encoder Ready")
print("=" * 50)


# ==================================================
# Text → Feature
# ==================================================

def generate_text_feature(text):

    tokens = tokenizer([text]).to(device)

    with torch.no_grad():

        feature = model.encode_text(tokens)

        feature /= feature.norm(dim=-1, keepdim=True)

    return feature.cpu().numpy()[0]


# ==================================================
# Search
# ==================================================

def search(cache, text, top_k=20):

    text_feature = generate_text_feature(text)

    scores = cache.features @ text_feature

    indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for idx in indices:

        results.append(
            SearchResult(
                image_id=cache.image_ids[idx],
                score=float(scores[idx]),
            )
        )

    return results