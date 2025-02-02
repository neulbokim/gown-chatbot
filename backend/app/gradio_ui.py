import sys
import os
import gradio as gr

# ✅ 현재 파일의 상위 디렉토리(`backend/`)를 Python 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils import check_gown_size  # ✅ backend.app.utils 대신 app.utils로 변경

def gradio_interface(name, student_id, phone):
    return check_gown_size(name, student_id, phone)

# ✅ Gradio 인터페이스 정의
gradio_app = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="이름"),
        gr.Textbox(label="학번"),
        gr.Textbox(label="전화번호"),
    ],
    outputs="text",
    title="🥼 가운 사이즈 조회 시스템",
    description="이름, 학번, 전화번호를 입력하면 가운 사이즈를 알려드립니다.",
    flagging_mode="never",
)

# ✅ Gradio 실행 함수
def run_gradio():
    gradio_app.launch(server_name="0.0.0.0", server_port=7860, share=True, show_error=True)
