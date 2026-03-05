import cv2 as cv
import numpy as np

# 초기 설정값
brush_size = 5
drawing = False # 마우스가 눌려진 상태인지 확인
color = (255, 0, 0) # 기본색: 파란색 (BGR)

# soccer 이미지 로드 (배경)
img = cv.imread(r'c:\opencv_\computer-vision\opencv\images\soccer.jpg')

if img is None:
    print("이미지를 불러올 수 없습니다. 경로를 확인해주세요.")
    exit()

def draw_circle(event, x, y, flags, param):
    global drawing, color, brush_size

    if event == cv.EVENT_LBUTTONDOWN: # 왼쪽 버튼 클릭
        drawing = True
        color = (255, 0, 0) # 파란색
        cv.circle(img, (x, y), brush_size, color, -1)

    elif event == cv.EVENT_RBUTTONDOWN: # 오른쪽 버튼 클릭
        drawing = True
        color = (0, 0, 255) # 빨간색
        cv.circle(img, (x, y), brush_size, color, -1)

    elif event == cv.EVENT_MOUSEMOVE: # 마우스 이동
        if drawing:
            cv.circle(img, (x, y), brush_size, color, -1)

    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP: # 버튼 뗌
        drawing = False

# 윈도우 생성 및 마우스 콜백 설정
cv.namedWindow('Drawing App')
cv.setMouseCallback('Drawing App', draw_circle)

print("--- 사용 방법 ---")
print("좌클릭: 파란색 / 우클릭: 빨간색")
print("+ : 붓 크기 증가 (최대 15)")
print("- : 붓 크기 감소 (최소 1)")
print("q : 종료")

while True:
    cv.imshow('Drawing App', img)
    
    key = cv.waitKey(1) & 0xFF

    # q 입력 시 종료
    if key == ord('q'):
        break
    
    # + 또는 = 입력 시 붓 크기 증가 (최대 15)
    elif key == ord('+') or key == ord('='):
        brush_size = min(15, brush_size + 1)
        print(f"현재 붓 크기: {brush_size}")
        
    # - 입력 시 붓 크기 감소 (최소 1)
    elif key == ord('-'):
        brush_size = max(1, brush_size - 1)
        print(f"현재 붓 크기: {brush_size}")

cv.destroyAllWindows()
