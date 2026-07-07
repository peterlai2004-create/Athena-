"""
Project Athena

Feature Manager Test
"""

from database import create_database
from feature_manager import process_features

conn, cursor = create_database()

process_features(cursor)

conn.commit()

conn.close()