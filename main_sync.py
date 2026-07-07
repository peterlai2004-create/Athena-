"""
Project Athena

Sync Test
"""

from database import create_database
from sync import compare


conn, cursor = create_database()

compare(cursor)

conn.close()