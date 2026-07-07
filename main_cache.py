"""
Project Athena

Feature Cache Test
"""

from database import create_database
from feature_cache import FeatureCache


conn, cursor = create_database()

cache = FeatureCache()

cache.load(cursor)

conn.close()