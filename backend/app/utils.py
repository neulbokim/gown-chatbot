import psycopg2
import re
from backend.config.settings import settings

# ✅ 전화번호 정규화 함수
def normalize_phone(phone: str) -> str:
    if not phone:
        return None
    phone = re.sub(r'\D', '', phone)  # 숫자만 남기기
    if len(phone) == 11 and phone.startswith("010"):
        return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
    return phone

# ✅ DB 연결 함수
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=settings.DB_HOST,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASS,
            port=settings.DB_PORT
        )
        return conn
    except Exception as e:
        print(f"❌ DB 연결 실패: {e}")
        return None

# ✅ 가운 사이즈 조회 함수
def check_gown_size(name: str, student_id: str, phone: str):
    conn = get_db_connection()
    if not conn:
        return "❌ DB 연결 오류"

    phone = normalize_phone(phone)  # 전화번호 정규화

    cursor = conn.cursor()
    cursor.execute(
        "SELECT gown_size FROM students WHERE name = %s AND student_id = %s AND phone = %s;",
        (name.strip(), student_id.strip(), phone.strip())
    )
    student = cursor.fetchone()
    cursor.close()
    conn.close()

    if student:
        return f"✅ {name}님의 가운 사이즈는 {student[0]}입니다!"
    else:
        return "❌ 입력한 정보와 일치하는 학생을 찾을 수 없습니다."
