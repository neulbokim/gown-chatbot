import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# CSV 데이터 불러오기
csv_path = "database/raw/preprocessed_2025 가운 신청.csv"
df = pd.read_csv(csv_path)

# DB 연결
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

# 데이터 삽입
insert_query = """
INSERT INTO students (name, student_id, phone, gown_size, gender, grade) 
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (student_id) DO NOTHING;
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row["이름"], row["학번"], row["전화번호"], row["가운 사이즈"], row["성별"], row["학년"]
    ))

conn.commit()
print("✅ 데이터 업로드 완료!")

# 연결 종료
cursor.close()
conn.close()
