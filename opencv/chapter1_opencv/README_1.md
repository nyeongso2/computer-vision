# 01. 이미지 불러오기 및 그레이스케일 변환

OpenCV를 사용하여 이미지를 불러오고, 원본 이미지와 그레이스케일로 변환된 이미지를 나란히 표시하는 실습입니다.

## 📂 파일 정보
*   **파일명**: `1.py`
*   **사용된 주요 함수**: `cv.imread()`, `cv.cvtColor()`, `np.hstack()`, `cv.imshow()`

## 코드 

```python
import cv2 as cv  # OpenCV 라이브러리를 cv라는 이름으로 임포트합니다.
import numpy as np  # 배열 및 수치 계산을 위한 numpy 라이브러리를 임포트합니다.

# 배경으로 사용할 축구공 이미지를 읽어옵니다. 
img = cv.imread(r'c:\opencv_\computer-vision\opencv\images\soccer.jpg')

if img is None:  # 이미지를 정상적으로 불러오지 못했다면 실행합니다.
    print("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")  # 에러 메시지를 출력합니다.
    exit()  # 프로그램을 종료합니다.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 원본 컬러 이미지(img)를 그레이스케일 이미지(gray)로 변환합니다.

# 원본 이미지와 그레이스케일 이미지를 가로 방향으로 합칩니다. 
# hstack은 수평 결합을 의미하며, 두 이미지의 높이가 같아야 합니다.
hybrid = np.hstack((img, gray))  # 합쳐진 이미지를 hybrid 변수에 저장합니다.

cv.imshow('Original vs Grayscale', hybrid)  # 'Original vs Grayscale'이라는 이름의 창에 합쳐진 이미지를 보여줍니다.

print("아무 키나 누르면 창이 닫힙니다.")  # 사용자에게 안내 메시지를 출력합니다.
cv.waitKey(0)  # 키보드 입력을 무한정 기다립니다. (0은 '무한대'를 의미)
cv.destroyAllWindows()  # 열려 있는 모든 윈도우 창을 닫고 프로그램을 종료합니다.
```



## 설명 


## 🖼 결과물 (`1_result.jpg`)
![alt text](image.png)



