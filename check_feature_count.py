from database import create_database

conn, cursor = create_database()

cursor.execute("""
SELECT COUNT(*)
FROM image_features
""")

print(cursor.fetchone()[0])

conn.close()