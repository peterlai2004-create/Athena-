"""
Project Athena

Search Engine Test
"""

from search_engine import generate_text_feature

feature = generate_text_feature(
    "white hair maid"
)

print(type(feature))

print(feature.shape)

print(feature[:10])