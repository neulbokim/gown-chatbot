import gradio as gr
from backend.app.main import check_gown_size

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
    allow_flagging="never",
)

# ✅ Gradio 실행 함수
def run_gradio():
    gradio_app.launch(server_name="0.0.0.0", server_port=7860, share=True, show_error=True)
