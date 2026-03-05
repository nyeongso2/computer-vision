import cv2 as cv  # OpenCV 라이브러리를 cv라는 이름으로 임포트합니다.
import numpy as np  # 배열 및 수치 계산을 위한 numpy 라이브러리를 임포트합니다.
import sys  # 프로그램 강제 종료(exit) 기능을 쓰기 위해 sys 모듈을 가져옵니다.

# cv.imread()를 사용하여 이미지 로드
img = cv.imread(r'c:\opencv_\computer-vision\opencv\images\soccer.jpg')

# 이미지 사이즈 축소
img = cv.resize(img, dsize=(0, 0), fx=0.5, fy=0.5)

if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")

else:
    # cv.cvtColor() 함수를 사용해 이미지를 그레이스케일로 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # np.hstack()을 위해 그레이스케일 이미지를 3채널(BGR)로 변환 (그래야 원본과 합쳐집니다)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

    # np.hstack() 함수를 이용해 원본이미지와 그레이스케일이미지를 가로로 연결
    result = np.hstack((img, gray_bgr))

    # cv.imshow()와 cv.waitKey()를 사용해 결과를 화면에 표시
    cv.imshow('Original and Grayscale', result)

    # 결과 이미지를 '1_result.jpg'로 저장
    cv.imwrite(r'c:\opencv_\computer-vision\opencv\1_result.jpg', result)

    # 사용자가 키보드에서 아무 키나 누를 때까지 프로그램을 무한히 기다리게 만듭니다.
    cv.waitKey(0)
    # 키를 누르는 순간 다음 줄로 넘어가면서, 열려 있던 모든 이미지 창을 한꺼번에 닫음
    cv.destroyAllWindows()
