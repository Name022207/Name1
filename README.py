pip install matplotlib

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv('GDP_성장률_실질__20250616122502')

# 웹앱 제목
st.title("🇰🇷 대한민국 GDP 시각화 웹앱")

# 연도별 GDP 라인 차트
st.subheader("연도별 실질 GDP 추이")
st.line_chart(df.set_index('year')['real_gdp'])

# 슬라이더로 연도 선택
year = st.slider("연도 선택", int(df['year'].min()), int(df['year'].max()))
gdp = df[df['year'] == year]['real_gdp'].values[0]
st.write(f"📌 {year}년 실질 GDP: **{gdp:.1f}조 원**")











