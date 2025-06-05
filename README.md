# GPS Ship Route Visualizer

이 저장소는 GPS 데이터를 활용하여 이동 경로를 지도 위에 시각화하는 두 가지 예제 코드를 제공합니다.
간단하고 빠르게 지도상에 GPS 데이터를 시각화하기 위한 코드입니다. 
경우에 따라서 자신의 데이터셋에 맞게 수정하여 사용하시길 바랍니다. 

## 주요 기능

### 1. gps_visualizer.py

CSV 형식의 GPS 데이터를 읽어와 Folium 지도를 활용해 선박의 이동 경로를 시각화합니다.

데이터 포인트 간 거리가 일정 거리 이상이면 선을 끊고 새로운 선을 시작합니다.

샘플링을 통해 데이터 크기를 효율적으로 관리하여 빠른 시각화가 가능합니다.

출력 파일: ship_route_separated.html

### 2. gps_visualizer_colored_dated.py

속도 데이터가 존재할 경우 속도 데이터(SHIP_SPD)에 따라 이동 경로를 다양한 색상으로 시각화하여 속도의 변화를 직관적으로 나타냅니다.

각 경로의 시작 지점과 종료 지점에 각각 빨간색과 파란색 마커를 추가합니다.

경로가 끊어지는 지점마다 시작 날짜를 지도상에 텍스트로 표시합니다.

출력 파일: ship_route_colored_dated.html

## 사용법

### 필수 라이브러리 설치
```
pip install pandas folium matplotlib haversine
pip install folium pandas
```
### 데이터 파일 준비
GPS 위경도 CSV 파일을 준비.

### 실행 예시
python gps_visualizer.py
python gps_visualizer_colored_dated.py

### 결과 HtML 파일
파일에서 선택하여 chrome과 같은 웹으로 실행하면 됩니다. 

본 코드의 sample 결과는 아래 링크의 "한나라호 선박의 운항경로 분석 데이터" (무료 공개, BigdataSea) 를 사용하였습니다. 
원본 샘플 데이터는 [BigdataSea](https://www.bigdata-sea.kr/datasearch/base/view.do?prodId=PROD_000082)에서 다운로드 할 수 있습니다.

## SAMPLE 결과
![sample1](https://github.com/user-attachments/assets/5c60f868-1a03-415a-a74c-7ecf64022e3c)




