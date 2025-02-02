import psycopg2
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# DB 연결
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    port=os.getenv("DB_PORT")
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
