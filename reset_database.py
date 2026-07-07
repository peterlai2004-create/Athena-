from database import create_database

conn, cursor = create_database()

cursor.execute("DELETE FROM image_features")
cursor.execute("DELETE FROM images")

conn.commit()

print("=" * 50)
print("Database Reset Complete")
print("=" * 50)

conn.close()