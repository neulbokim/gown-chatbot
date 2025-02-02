import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

print("🔹 DB_USER:", os.getenv("DB_USER"))  # DB_USER 값 확인

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    
    # 커서 생성
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print("✅ 연결 성공! PostgreSQL 버전:", db_version)
    
    # 연결 종료
    cursor.close()
    conn.close()

except Exception as e:
    print("❌ 연결 실패:", e)
