import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 데이터 준비 (리스트)
years = [
1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,
1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,
2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,
2020,2021,2022,2023,2024,2025
]

gdps = [
65.4,72.9,78.4,87.8,97.5,101.3,116.8,148.0,199.6,246.9,
283.4,330.7,355.5,392.7,463.6,566.6,610.2,569.8,383.3,497.5,
576.2,547.7,627.2,702.7,793.2,934.9,1053.2,1172.6,1047.3,943.9,
1143.7,1253.3,1278.1,1370.6,1484.5,1466.0,1499.7,1623.1,1725.4,1651.4,
1644.3,1818.4,1673.9,1712.8,1812.5,1850.0
]

# 2. DataFrame 생성
df = pd.DataFrame({
    'Year': years,
    'GDP (USD Billions)': gdps
})

# 3. Streamlit 앱 구성
st.title('대한민국 GDP 변화 (1980-2025)')

# 데이터 테이블 보여주기
st.dataframe(df)

# 선 그래프 그리기
fig, ax = plt.subplots()
ax.plot(df['Year'], df['GDP (USD Billions)'], marker='o', linestyle='-')
ax.set_xlabel('Year')
ax.set_ylabel('GDP (USD Billions)')
ax.set_title('대한민국 GDP 변화 추이')
ax.grid(True)

st.pyplot(fig)

# 4. CSV 파일 다운로드 링크 제공
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="GDP 데이터 CSV 다운로드",
    data=csv,
    file_name='gdp_korea.csv',
    mime='text/csv',
)

