import psycopg2
from config.settings import settings

# DB 연결
conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        port=settings.DB_PORT
    )
cursor = conn.cursor()

# 데이터 조회 (성별 및 학년 포함)
query = "SELECT * FROM students;"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# 연결 종료
cursor.close()
conn.close()
