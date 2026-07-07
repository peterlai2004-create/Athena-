from database import create_database
from config import AI_MODEL

conn, cursor = create_database()

cursor.execute(
    """
    SELECT
        COUNT(*)
    FROM images

    LEFT JOIN image_features
    ON images.id = image_features.image_id
       AND image_features.model = ?

    WHERE image_features.id IS NULL
    """,
    (AI_MODEL,),
)

print("Pending :", cursor.fetchone()[0])

conn.close()