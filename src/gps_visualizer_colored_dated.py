import pandas as pd
import folium
from haversine import haversine
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# 데이터 로드
df = pd.read_csv('Hannara_ship_trajactory.csv')

# 1000개씩 샘플링
df_sampled = df.iloc[::1000]

# 중심점 설정
map_center = [df_sampled['LA'].mean(), df_sampled['LO'].mean()]
m = folium.Map(location=map_center, zoom_start=9)

# 속도에 따른 컬러맵 설정
min_speed, max_speed = df_sampled['SHIP_SPD'].min(), df_sampled['SHIP_SPD'].max()
norm = colors.Normalize(vmin=min_speed, vmax=max_speed)
cmap = plt.colormaps['jet']

# 최대 허용 거리 설정 (km)
max_distance = 20

coords = list(zip(df_sampled['LA'], df_sampled['LO']))
speeds = df_sampled['SHIP_SPD'].tolist()
dates = df_sampled['MSRM_DTM'].tolist()

# 첫 번째 segment 초기화
line_segment = [coords[0]]
speed_segment = [speeds[0]]
start_date = dates[0]

for i in range(1, len(coords)):
    distance = haversine(coords[i - 1], coords[i])

    if distance < max_distance:
        line_segment.append(coords[i])
        speed_segment.append(speeds[i])
    else:
        # 현재 segment 지도에 추가 (평균 속도로 색상 결정)
        avg_speed = sum(speed_segment) / len(speed_segment)
        line_color = colors.to_hex(cmap(norm(avg_speed)))
        folium.PolyLine(line_segment, color=line_color, weight=3, opacity=0.8).add_to(m)

        # 시작점과 종료점 마커 추가
        folium.Marker(line_segment[0], icon=folium.Icon(color='red'), popup='Start').add_to(m)
        folium.Marker(line_segment[-1], icon=folium.Icon(color='blue'), popup='End').add_to(m)

        # 선이 끊길 때 날짜 텍스트 추가
        folium.Marker(
            location=line_segment[-1],
            icon=folium.DivIcon(
                html=f'<div style="font-size:12px; font-weight:bold;">{start_date}</div>'
            )
        ).add_to(m)

        # 새로운 segment 시작
        line_segment = [coords[i]]
        speed_segment = [speeds[i]]
        start_date = dates[i]

# 마지막 segment 추가
if len(line_segment) > 1:
    avg_speed = sum(speed_segment) / len(speed_segment)
    line_color = colors.to_hex(cmap(norm(avg_speed)))
    folium.PolyLine(line_segment, color=line_color, weight=3, opacity=0.8).add_to(m)

    # 시작점과 종료점 마커 추가
    folium.Marker(line_segment[0], icon=folium.Icon(color='red'), popup='Start').add_to(m)
    folium.Marker(line_segment[-1], icon=folium.Icon(color='blue'), popup='End').add_to(m)

    # 마지막 segment 날짜 추가
    folium.Marker(
        location=line_segment[-1],
        icon=folium.DivIcon(
            html=f'<div style="font-size:12px; font-weight:bold;">{start_date}</div>'
        )
    ).add_to(m)

# 지도 저장
m.save('ship_route_colored_dated.html')