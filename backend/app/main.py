# ✅ 반드시 위쪽에서 utils.py import
from backend.app.utils import check_gown_size

from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel

app = FastAPI()

@app.get("/gown_size")
def get_gown_size(name: str, student_id: str, phone: str):
    return {"message": check_gown_size(name, student_id, phone)}

@app.get("/")
def home():
    return {"message": "가운 사이즈 조회 API 입니다. 웹 UI를 이용하세요."}
