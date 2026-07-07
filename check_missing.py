from database import create_database

conn, cursor = create_database()

cursor.execute("""
SELECT images.path
FROM images

LEFT JOIN image_features
ON images.id = image_features.image_id

WHERE image_features.id IS NULL
""")

rows = cursor.fetchall()

print("Missing:", len(rows))

for row in rows:
    print(row[0])

conn.close()