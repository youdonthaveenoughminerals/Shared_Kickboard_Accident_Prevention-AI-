# 공식 Python 3.10 이미지 사용 (경량화된 Slim 버전)
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치 (캐싱 최적화)
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY app.py .

# Streamlit 기본 포트 8501 노출
EXPOSE 8501

# 애플리케이션 실행
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
