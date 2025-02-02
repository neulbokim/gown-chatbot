from fastapi import FastAPI, HTTPException, Query
import psycopg2
import os
from dotenv import load_dotenv

# FastAPI 앱 생성
app = FastAPI()

# .env 파일 로드
load_dotenv()

# DB 연결 함수
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )

# ✅ 1. 학생 정보 조회 API (기존)
@app.get("/student/{student_id}")
def get_student(student_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE student_id = %s;", (student_id,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    if student:
        return {
            "id": student[0],
            "name": student[1],
            "student_id": student[2],
            "phone": student[3],
            "gown_size": student[4],
            "gender": student[5],
            "grade": student[6]
        }
    else:
        raise HTTPException(status_code=404, detail="학생을 찾을 수 없습니다.")

# ✅ 2. "가운 사이즈 확인" API (이름, 학번, 전화번호 입력)
@app.get("/check_gown_size")
def check_gown_size(
    name: str = Query(..., description="학생 이름"),
    student_id: str = Query(..., description="학생 학번"),
    phone: str = Query(..., description="학생 전화번호")
):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 학생 정보 조회 쿼리
    cursor.execute(
        "SELECT gown_size FROM students WHERE name = %s AND student_id = %s AND phone = %s;",
        (name, student_id, phone)
    )
    student = cursor.fetchone()

    cursor.close()
    conn.close()

    if student:
        return {
            "message": f"{name}님의 가운 사이즈는 {student[0]}입니다."
        }
    else:
        raise HTTPException(status_code=404, detail="입력한 정보와 일치하는 학생이 없습니다.")
