from database import create_database

conn, cursor = create_database()

cursor.execute("""
SELECT COUNT(*)
FROM image_features
""")

print("Features :", cursor.fetchone()[0])

conn.close()