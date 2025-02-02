import os
from dotenv import load_dotenv

# ✅ .env 파일 로드
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

class Settings:
    """환경 변수를 관리하는 설정 클래스"""
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_PORT = os.getenv("DB_PORT")

# ✅ Settings 인스턴스 생성
settings = Settings()
