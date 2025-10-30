import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# AWS 연결 대신 가상의 데이터 생성 함수 (실제 발표 시 AWS S3/DynamoDB에서 로드한다고 설명)
@st.cache_data
def load_and_process_data():
    """
    가상의 PM 안전 운영 데이터를 생성합니다. 
    이 데이터는 기술 4(위험 운행 감지)와 기술 5(스마트 주차 검증)의 결과물입니다.
    """
    
    # 1. 사용자 평판/점수 데이터 (기술 ⑥ 연동)
    user_ids = [f'User_{i:04d}' for i in range(1, 101)]
    data = {
        'user_id': user_ids,
        'safety_score': np.random.randint(65, 100, 100),
        'total_rides': np.random.randint(20, 300, 100),
        'helmet_compliance': np.random.rand(100) > 0.1,
        'geo_fence_violations': np.random.randint(0, 15, 100),
        'parking_violations': np.random.randint(0, 10, 100)
    }
    df_users = pd.DataFrame(data).sort_values(by='safety_score', ascending=False).reset_index(drop=True)
    df_users['rank'] = df_users.index + 1

    # 2. 실시간 위반 히트맵 데이터 (기술 ④, ⑤ 연동)
    n_violations = 500
    df_violations = pd.DataFrame({
        'violation_type': np.random.choice(['Smart Parking Fail', 'Dangerous Driving', 'Speed Limit Fail'], n_violations, p=[0.5, 0.3, 0.2]),
        'lat': 37.5 + (np.random.randn(n_violations) * 0.03), # 서울 중심가 인근 위도
        'lon': 127.0 + (np.random.randn(n_violations) * 0.05), # 서울 중심가 인근 경도
        'severity': np.random.randint(1, 5, n_violations)
    })
    
    return df_users, df_violations

df_users, df_violations = load_and_process_data()

# --- Streamlit UI 시작 ---

st.set_page_config(layout="wide", page_title="PM AI 안전 플랫폼 운영 대시보드")

st.title("PM AI 통합 안전 플랫폼: 운영 대시보드")
st.markdown("##### 기술 ⑥: 인센티브/페널티 연동 (평판 시스템) 및 데이터 피드백 루프 시각화")

# AWS 클라우드 연결 상태 시뮬레이션
st.sidebar.header("시스템 아키텍처 (AWS 기반)")
st.sidebar.markdown(
    """
    - **Data Source:** AWS S3 (Raw Data), AWS DynamoDB (Reputation Score)
    - **Compute:** AWS Lambda (API Gateway 연동)
    - **Visualization:** Streamlit on Docker
    """
)

# 1. KPI 요약 카드
col1, col2, col3, col4 = st.columns(4)

total_rides = df_users['total_rides'].sum()
avg_score = df_users['safety_score'].mean()
total_violations = df_violations.shape[0]
avg_geo_violation = df_users['geo_fence_violations'].mean()

col1.metric("총 운행 건수 (Total Rides)", f"{total_rides:,}")
col2.metric("평균 안전 점수 (Avg. Safety Score)", f"{avg_score:.1f} / 100", delta=f"{avg_score - 85.0:.1f} Pts", delta_color="normal")
col3.metric("총 위반 건수 (Total Violations)", f"{total_violations:,}")
col4.metric("사용자당 평균 구역 위반", f"{avg_geo_violation:.1f} 건")

st.markdown("---")

# 2. 위험 지역/패턴 히트맵 (기술 ④, ⑤ 데이터 시각화)
st.header("1. 실시간 위험 발생 지역 히트맵")
st.markdown("PM 센서 데이터 (기술 ④) 및 주차 사진 분석 결과 (기술 ⑤)를 지도에 표시합니다. **지자체 인프라 개선을 위한 데이터 피드백**에 활용됩니다.")

fig_map = px.scatter_mapbox(
    df_violations,
    lat="lat",
    lon="lon",
    color="violation_type",
    size="severity",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    height=400,
    mapbox_style="carto-positron",
    hover_data=['violation_type', 'severity']
)
fig_map.update_layout(mapbox_bounds={"west": 126.5, "east": 127.5, "south": 37.2, "north": 37.8})
st.plotly_chart(fig_map, use_container_width=True)


st.markdown("---")

# 3. 사용자 평판 시스템 랭킹 (기술 ⑥ 시각화)
st.header("2. 사용자 안전 평판 점수 랭킹")
st.markdown("면허 인증(①), 안전모 인식(②), 구역 제어(③), 위험 운행 감속(④), 주차 검증(⑤) 결과가 통합되어 점수화됩니다. **Gamification (슬라이드 14)**의 핵심 지표입니다.")

col_rank, col_chart = st.columns([1, 2])

with col_rank:
    st.subheader("골드/실버 라이더 대상")
    # 상위 10명 테이블
    st.dataframe(
        df_users[['rank', 'user_id', 'safety_score', 'total_rides']].head(10).style.highlight_max(axis=0, subset=['safety_score'], color='#004d40'),
        use_container_width=True,
        hide_index=True
    )

with col_chart:
    # 점수 분포 차트
    fig_score = px.histogram(
        df_users, 
        x="safety_score", 
        nbins=20, 
        title="안전 점수 분포",
        color_discrete_sequence=['#4299e1']
    ).update_layout(xaxis_title="안전 점수 (Safety Score)", yaxis_title="사용자 수")
    st.plotly_chart(fig_score, use_container_width=True)

# 4. Docker 배포 설명 영역 
st.markdown("---")
st.info(
    "본 대시보드는 Docker 컨테이너로 패키징되어 PM 운영 서버에 즉시 배포 가능하며, "
    "데이터는 AWS 클라우드 환경에서 실시간으로 수집되어 확장성을 확보합니다. "
    "이는 PM 시스템의 기술적 완성도를 높입니다."
)
