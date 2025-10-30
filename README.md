🛴 PM (개인형 이동수단) 안전 증진을 위한 AI 제어 시스템 & 데이터 대시보드
1. 프로젝트 개요 (Overview)
본 프로젝트는 급증하는 개인형 이동수단(PM) 사고 및 무단 주차 문제를 해결하기 위해, AI 기술 기반의 PM 안전 제어 로직을 구현하고 이를 지원하는 운영 현황 시각화 대시보드를 통합 개발합니다.
목표: PM 서비스의 안전성, 법규 준수율, 운영 효율성을 극대화하여 지속 가능한 공유 경제 생태계 구축에 기여합니다.
핵심 가치: 6단계 AI 안전 제어 시스템 데모와 데이터 기반의 인사이트를 통합 제공.
2. 주요 구성 요소 (Key Components)
2.1. 📊 운영 현황 데이터 대시보드 (백엔드: app.py)
Python Streamlit을 사용하여 구현된 대화형 대시보드입니다. PM 운영 데이터를 분석하여 위험 요소와 운영 효율 지표를 실시간으로 모니터링합니다.
사고 데이터 분석: 월별/연령별 사고 트렌드 시각화 ([한국도로교통공단_개인형이동수단(PM)교통사고 발생월별 가해연령별 현황_20221231.csv 등 데이터 활용]).
위험 운행 감지: 위험 운행/주차 위반 발생 구역 지도 시각화.
사용자 평판 시스템: 안전 점수 랭킹 및 상벌점 현황 시각화.
2.2. 🤖 AI 안전 제어 시스템 UI 데모 (프론트엔드: AI 기반 PM 안전 시스템 시연.html)
6단계 AI 안전 로직의 작동 원리를 보여주는 단일 HTML 기반의 시뮬레이션 UI입니다. 사용자는 각 단계별 AI가 어떻게 PM 운행을 통제하는지 체험할 수 있습니다.
단계
기능
AI 기술
1단계
면허/본인 인증
OCR, 안면 인식
2단계
안전모 착용 감지
객체 감지 및 자세 추정
3단계
위험 구역 자동 제어
지오펜싱 및 속도 제어
4단계
위험 운행 자동 감속
시계열 센서 데이터 분석
5단계
스마트 주차 검증
이미지 객체 및 위치 파악
6단계
사용자 평판 관리
행동 분석 및 데이터 누적

3. 기술 스택 (Tech Stack)
구분
기술 스택
설명
컨테이너
Docker, Docker Compose (Dockerfile)
프로젝트 환경 의존성 제거 및 쉬운 배포.
데이터 대시보드
Python, Streamlit, Pandas, Plotly
데이터 처리 및 실시간 시각화.
프론트엔드/데모
HTML5, Tailwind CSS, JavaScript
AI 시연 UI 구현.
의존성 관리
requirements.txt
Python 패키지 의존성 명시.

4. 시작하기 (Getting Started)
프로젝트는 Docker를 사용하여 모든 의존성을 포함하고 있습니다. 다음 단계를 따르면 대시보드와 UI 데모를 동시에 실행할 수 있습니다.
4.1. 선행 조건 (Prerequisites)
Docker 및 Docker Compose 설치
Git 설치
4.2. 설치 및 실행 (Installation & Run)
저장소 복제:
git clone [https://github.com/youdonthaveenoughminerals/Shared_Kickboard_Accident_Prevention-AI-/]
cd [Shared_Kickboard_Accident_Prevention-AI-/]


Docker Compose 파일 생성 및 실행:
Dockerfile, requirements.txt, app.py 파일을 기반으로 서비스를 묶어 실행할 docker-compose.yml 파일을 작성합니다. (이 파일이 있다면 생략하고 3단계로 이동하세요.)
서비스 실행:
# (주의: 만약 docker-compose.yml 파일이 없고, app.py만 실행한다면)
# docker-compose up --build -d  (Docker Compose 사용 시)
# 또는
docker build -t pm-dashboard .
docker run -d -p 8501:8501 pm-dashboard


참고: Dockerfile에는 Streamlit이 8501 포트로 실행되도록 설정되어 있습니다.
접속:
운영 데이터 대시보드: 브라우저에서 http://localhost:8501 에 접속합니다.
AI 제어 시스템 UI 데모: 프로젝트 폴더 내의 AI 기반 PM 안전 시스템 시연.html 파일을 직접 브라우저로 열어 실행합니다.
5. 프로젝트 구조 (Project Structure)
.
├── Dockerfile                  # Python 환경 및 Streamlit 실행 설정
├── requirements.txt            # Python 의존성 목록 (streamlit, pandas, plotly 등)
├── app.py                      # (Python) Streamlit 기반 데이터 대시보드 애플리케이션
├── AI 기반 PM 안전 시스템 시연.html # (HTML/JS) 6단계 AI 제어 시스템 시연 UI
├── pm_age_data.xlsx
└── pm_age_data.csv           # 분석에 사용된 원본 데이터 파일들



6. 기여 (Contributing)
버그 리포트, 기능 제안 및 코드 기여는 언제나 환영합니다.
Pull Request를 생성하기 전에 이슈를 통해 논의해 주시면 감사하겠습니다.
7. 라이선스
이 프로젝트는 [라이선스 명시 (예: MIT License)]를 따릅니다.
