"""
Project Athena

feature_engine.py

OpenCLIP Feature Engine
"""

import open_clip
import torch

from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

print("=" * 50)
print("Loading OpenCLIP...")

model, preprocess, tokenizer = open_clip.create_model_and_transforms(
    "ViT-B-32",
    pretrained="laion2b_s34b_b79k",
)

model = model.to(device)
model.eval()

print("OpenCLIP Ready")
print("=" * 50)


def generate_feature(image_path):

    image = preprocess(
        Image.open(image_path)
    ).unsqueeze(0).to(device)

    with torch.no_grad():

        feature = model.encode_image(image)

        feature /= feature.norm(dim=-1, keepdim=True)

    return feature.cpu().numpy().tobytes()