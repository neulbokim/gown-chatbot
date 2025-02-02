import psycopg2
from config.settings import settings

def create_students_table():
    """students 테이블이 없으면 한 번에 모든 컬럼을 생성"""
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        port=settings.DB_PORT
    )
    cursor = conn.cursor()

    # ✅ students 테이블 생성 (존재하지 않을 경우)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        student_id VARCHAR(20) UNIQUE NOT NULL,
        phone VARCHAR(20) NOT NULL,
        gown_size VARCHAR(10) NOT NULL,
        gender VARCHAR(10),  
        grade INT             
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("✅ students 테이블 생성 완료 (모든 컬럼 포함)!")

    cursor.close()
    conn.close()
    print("🎉 모든 테이블 & 컬럼 업데이트 완료!")

if __name__ == "__main__":
    create_students_table()
