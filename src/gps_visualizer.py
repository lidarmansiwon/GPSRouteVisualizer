import pandas as pd
import folium
from haversine import haversine

# 데이터 로드
df = pd.read_csv('Hannara_ship_trajactory.csv')

# 500개씩 샘플링
df_sampled = df.iloc[::500]

# 중심점
map_center = [df_sampled['LA'].mean(), df_sampled['LO'].mean()]
m = folium.Map(location=map_center, zoom_start=9)

# 기준 거리 (km), 이 거리보다 멀어지면 끊고 다시 선을 시작
max_distance = 5  # km 단위, 필요에 따라 변경 가능

# 좌표 데이터 준비
coords = list(zip(df['LA'], df['LO']))

# 경로 초기화
line_segment = [coords[0]]

for i in range(1, len(coords)):
    prev_coord = coords[i - 1]
    curr_coord = coords[i]

    distance = haversine(prev_coord, curr_coord)

    if distance < max_distance:
        line_segment.append(curr_coord)
    else:
        # 거리가 멀어지면 현재까지 선을 지도에 그리고 새로운 세그먼트 시작
        folium.PolyLine(line_segment, color='blue', weight=3, opacity=0.8).add_to(m)
        line_segment = [curr_coord]

# 마지막 세그먼트 추가
if len(line_segment) > 1:
    folium.PolyLine(line_segment, color='blue', weight=3, opacity=0.8).add_to(m)

m.save('ship_route_separated.html')
