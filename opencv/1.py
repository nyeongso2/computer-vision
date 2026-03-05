import cv2 as cv
import numpy as np

# 1. cv.imread()를 사용하여 이미지 로드
img = cv.imread(r'c:\opencv_\computer-vision\opencv\images\soccer.jpg')

img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")

else:
    # 2. cv.cvtColor() 함수를 사용해 이미지를 그레이스케일로 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # np.hstack()을 위해 그레이스케일 이미지를 3채널(BGR)로 변환 (그래야 원본과 합쳐집니다)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # 3. np.hstack() 함수를 이용해 원본이미지와 그레이스케일이미지를 가로로 연결
    result = np.hstack((img, gray_bgr))

    # 4. cv.imshow()와 cv.waitKey()를 사용해 결과를 화면에 표시
    cv.imshow('Original and Grayscale', result)

    # 아무 키나 누르면 창이 닫히도록 설정
    cv.waitKey(0)
    cv.destroyAllWindows()
