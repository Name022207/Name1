import matplotlib.pyplot as plt

# 연도별 GDP 데이터
years = list(range(1980, 2026))
gdp_values = [
    65.4, 72.9, 78.4, 87.8, 97.5, 101.3, 116.8, 148.0, 199.6, 246.9, 283.4, 330.7, 355.5, 392.7, 463.6, 566.6,
    610.2, 569.8, 383.3, 497.5, 576.2, 547.7, 627.2, 702.7, 793.2, 934.9, 1053.2, 1172.6, 1047.3, 943.9, 1143.7,
    1253.3, 1278.1, 1370.6, 1484.5, 1466.0, 1499.7, 1623.1, 1725.4, 1651.4, 1644.3, 1818.4, 1673.9, 1712.8, 1812.5, 1850.0
]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(years, gdp_values, marker='o', linestyle='-', color='b', label='GDP (USD Billions)')
plt.title('South Korea GDP (1980–2025)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP (USD Billions)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
