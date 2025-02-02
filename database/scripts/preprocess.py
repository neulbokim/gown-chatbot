import pandas as pd
import re
import os

class GownDataPreprocessor:
    def __init__(self, raw_data_dir, input_filename):
        """
        데이터 전처리를 위한 클래스
        :param raw_data_dir: 원본 데이터 폴더 경로
        :param input_filename: 원본 데이터 파일명
        """
        self.raw_data_dir = raw_data_dir
        self.input_filename = input_filename
        self.input_path = os.path.join(raw_data_dir, input_filename)
        self.output_filename = f"preprocessed_{input_filename}"
        self.output_path = os.path.join(raw_data_dir, self.output_filename)
        
    def normalize_phone(self, phone):
        """
        전화번호를 010-xxxx-xxxx 형식으로 변환
        :param phone: 원본 전화번호 문자열
        :return: 변환된 전화번호
        """
        if pd.isna(phone):
            return None  # NaN 값은 변환하지 않음
        
        phone = re.sub(r'\D', '', phone)  # 숫자만 남기기
        
        # 10자리 (예: 1012345678) → 앞에 0을 추가하여 11자리로 맞추기
        if len(phone) == 10:
            phone = "0" + phone  # 앞에 0을 추가하여 11자리로 변환

        # 11자리 정상 전화번호 변환
        if len(phone) == 11 and phone.startswith("010"):
            return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
        
        return phone  # 변환할 수 없는 경우 그대로 반환

    def convert_grade(self, grade):
        """
        학년을 숫자로 변환 (예과 1학년 → 1, 본과 3학년 → 5)
        :param grade: 원본 학년 문자열
        :return: 변환된 학년 숫자 (변환 실패 시 None)
        """
        grade_mapping = {
            "예과 1학년": 1,
            "예과 2학년": 2,
            "본과 1학년": 3,
            "본과 2학년": 4,
            "본과 3학년": 5,
            "본과 4학년": 6
        }

        # 문자열인지 확인하고, 매핑된 값 반환
        if isinstance(grade, str) and grade in grade_mapping:
            return grade_mapping[grade]
        
        return None  # 변환할 수 없는 경우 None 반환

    def preprocess_data(self):
        """
        CSV 데이터를 불러와 전처리 후 변환된 데이터를 반환
        :return: 전처리된 DataFrame
        """
        # 데이터 불러오기
        df = pd.read_csv(self.input_path)

        # 필요한 컬럼 선택 (이메일 제외)
        df = df[['이름', '학번', '학년', '성별', '가운 사이즈', '전화번호']]

        # 전화번호 변환
        df['전화번호'] = df['전화번호'].astype(str).apply(self.normalize_phone)

        # 학년 변환
        df['학년'] = df['학년'].apply(self.convert_grade)

        return df

    def save_preprocessed_data(self, df):
        """
        변환된 데이터를 CSV 파일로 저장
        :param df: 전처리된 DataFrame
        """
        df.to_csv(self.output_path, index=False, encoding='utf-8-sig')
        print(f"✅ 전처리 완료! 변환된 파일이 '{self.output_path}'에 저장되었습니다.")

    def run(self):
        """
        전체 전처리 프로세스를 실행
        """
        df = self.preprocess_data()
        self.save_preprocessed_data(df)


# 🔹 실행 코드
if __name__ == "__main__":
    # 현재 스크립트 파일(`preprocess.py`)의 위치를 기준으로 `database/raw` 경로 설정
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # `database/` 폴더 경로
    raw_data_dir = os.path.join(base_dir, "raw")  # `database/raw/` 폴더 경로
    input_filename = "2025 가운 신청.csv"

    preprocessor = GownDataPreprocessor(raw_data_dir, input_filename)
    preprocessor.run()
