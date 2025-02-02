import psycopg2
import pandas as pd
import os
from config.settings import settings  # 변경: settings.py 사용

# ✅ 1. CSV 데이터 불러오기 (절대 경로 사용)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # backend/ 상위 폴더
csv_path = os.path.join(base_dir, "database/raw/preprocessed_2025 가운 신청.csv")

try:
    df = pd.read_csv(csv_path)
    print(f"✅ {len(df)}개의 데이터를 불러왔습니다.")
except FileNotFoundError:
    print("❌ CSV 파일을 찾을 수 없습니다.")
    exit()

# ✅ 2. DB 연결
try:
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        port=settings.DB_PORT
    )
    cursor = conn.cursor()
    print("✅ DB 연결 성공!")
except Exception as e:
    print(f"❌ DB 연결 실패: {e}")
    exit()

# ✅ 3. 데이터 삽입 (이미 존재하는 `student_id`는 정보 업데이트)
insert_query = """
INSERT INTO students (name, student_id, phone, gown_size, gender, grade) 
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (student_id) 
DO UPDATE SET 
    name = EXCLUDED.name,
    phone = EXCLUDED.phone,
    gown_size = EXCLUDED.gown_size,
    gender = EXCLUDED.gender,
    grade = EXCLUDED.grade;
"""

# ✅ 4. 데이터 삽입 수행
try:
    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            row["이름"], row["학번"], row["전화번호"], row["가운 사이즈"], row["성별"], row["학년"]
        ))
    conn.commit()
    print("✅ 데이터 업로드 완료!")
except Exception as e:
    print(f"❌ 데이터 삽입 중 오류 발생: {e}")
    conn.rollback()

# ✅ 5. 연결 종료
cursor.close()
conn.close()
print("✅ DB 연결 종료")
