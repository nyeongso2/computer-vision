import cv2 as cv
import numpy as np

# 초기 상태 설정
is_dragging = False
x_start, y_start = -1, -1
roi = None

# 이미지 로드
img_path = r'c:\opencv_\computer-vision\opencv\images\soccer.jpg'
img = cv.imread(img_path)
if img is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

img_original = img.copy() # 원본 보존

def on_mouse(event, x, y, flags, param):
    global is_dragging, x_start, y_start, img, roi

    if event == cv.EVENT_LBUTTONDOWN: # 클릭 시작
        is_dragging = True
        x_start, y_start = x, y

    elif event == cv.EVENT_MOUSEMOVE: # 드래그 중
        if is_dragging:
            img_draw = img_original.copy() # 실시간으로 사각형 그리기
            cv.rectangle(img_draw, (x_start, y_start), (x, y), (0, 255, 0), 2)
            cv.imshow('ROI Selection', img_draw)

    elif event == cv.EVENT_LBUTTONUP: # 클릭 종료
        is_dragging = False
        x_end, y_end = x, y
        
        # 좌표 정렬 (거꾸로 드래그했을 때 대비)
        left = min(x_start, x_end)
        top = min(y_start, y_end)
        right = max(x_start, x_end)
        bottom = max(y_start, y_end)

        if right > left and bottom > top:
            # ROI 추출 (Numpy 슬라이싱)
            roi = img_original[top:bottom, left:right]
            cv.imshow('Selected ROI', roi)
            # 메인 창에도 선택 영역 표시
            temp_img = img_original.copy()
            cv.rectangle(temp_img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv.imshow('ROI Selection', temp_img)

# 윈도우 생성 및 콜백 설정
cv.namedWindow('ROI Selection')
cv.setMouseCallback('ROI Selection', on_mouse)

print("--- 사용 방법 ---")
print("드래그 : 영역 선택")
print("r : 영역 선택 리셋")
print("s : 선택 영역 저장")
print("q : 종료")

while True:
    cv.imshow('ROI Selection', img)
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'): # q: 종료
        break
    
    elif key == ord('r'): # r: 리셋
        img = img_original.copy()
        roi = None
        if cv.getWindowProperty('Selected ROI', cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow('Selected ROI')
        print("리셋되었습니다.")

    elif key == ord('s'): # s: 저장
        if roi is not None:
            save_path = r'c:\opencv_\computer-vision\opencv\roi.jpg'
            cv.imwrite(save_path, roi)
            print(f"선택 영역이 {save_path}로 저장되었습니다.")
        else:
            print("저장할 영역이 없습니다. 먼저 마우스로 드래그하세요.")

cv.destroyAllWindows()
