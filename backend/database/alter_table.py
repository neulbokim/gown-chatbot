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

# 테이블 수정 쿼리 (성별과 학년 추가)
alter_table_query = """
ALTER TABLE students 
ADD COLUMN gender VARCHAR(10),
ADD COLUMN grade INT;
"""
try:
    cursor.execute(alter_table_query)
    conn.commit()
    print("✅ students 테이블 수정 완료! (성별, 학년 추가됨)")
except psycopg2.errors.DuplicateColumn:
    print("⚠️ 이미 gender 및 grade 컬럼이 존재합니다.")

# 연결 종료
cursor.close()
conn.close()
