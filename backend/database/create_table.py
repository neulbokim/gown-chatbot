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

# 테이블 생성 쿼리
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    gown_size VARCHAR(10) NOT NULL
);
"""
cursor.execute(create_table_query)
conn.commit()

print("✅ 테이블 생성 완료!")

# 연결 종료
cursor.close()
conn.close()
