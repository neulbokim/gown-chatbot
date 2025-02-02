import psycopg2
from config.settings import settings

def get_db_connection():
    """
    AWS RDS PostgreSQL 연결을 설정하는 함수
    :return: 연결된 psycopg2 connection 객체 또는 None
    """
    try:
        conn = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASS,
            port=settings.DB_PORT
        )
        return conn  # ✅ 연결된 DB 객체 반환
    except Exception as e:
        print("❌ DB 연결 실패:", e)
        return None  # ❌ 연결 실패 시 None 반환

def test_db_connection():
    """
    PostgreSQL 연결 테스트 함수 (DB 버전 확인)
    """
    conn = get_db_connection()
    if conn is None:
        print("❌ DB 연결에 실패하여 테스트를 진행할 수 없습니다.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("✅ PostgreSQL 연결 성공! 버전:", db_version[0])
    except Exception as e:
        print("❌ DB 테스트 중 오류 발생:", e)
    finally:
        cursor.close()
        conn.close()

# ✅ 직접 실행 시 DB 연결 테스트 수행
if __name__ == "__main__":
    test_db_connection()
