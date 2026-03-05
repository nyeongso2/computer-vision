import cv2 as cv  # OpenCV 라이브러리를 cv라는 이름으로 임포트합니다.
import numpy as np  # 배열 및 수치 계산을 위한 numpy 라이브러리를 임포트합니다.
import sys  # 프로그램 강제 종료(exit) 기능을 쓰기 위해 sys 모듈을 가져옵니다.

# --- 프로그램 상태 제어를 위한 변수 초기화 ---
is_dragging = False  # 마우스를 누른 채 움직이는 '드래그' 상태인지 저장하는 변수입니다.
x_start, y_start = -1, -1  # 드래그를 시작한 위치의 X, Y 좌표를 저장할 공간입니다.
roi = None  # 마우스로 선택해서 잘라낸 관심 영역(ROI) 이미지를 담을 변수입니다.

# --- 배경 이미지 로드 ---
img_path = r'c:\opencv_\computer-vision\opencv\images\soccer.jpg'  # 사용할 이미지의 절대 경로입니다.
img_original = cv.imread(img_path)  # 해당 경로의 이미지를 읽어 img_original에 저장합니다.

if img_original is None:  # 이미지 파일이 없거나 읽기에 실패했을 경우 실행합니다.
    print("이미지를 불러올 수 없습니다.")  # 터미널에 에러 메시지를 출력합니다.
    sys.exit()  # 프로그램 실행을 여기서 즉시 중단합니다.

# --- 화면 출력용 버퍼 생성 ---
img_display = img_original.copy()  # 원본을 건드리지 않기 위해 화면 표시용 복사본을 만듭니다.

def on_mouse(event, x, y, flags, param):  # 마우스 이벤트가 발생할 때 호출되는 함수입니다.
    global is_dragging, x_start, y_start, img_display, roi  # 전역 변수들을 함수 내에서 수정합니다.

    if event == cv.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼을 눌렀을 때 실행됩니다.
        is_dragging = True  # 드래그가 시작되었음을 True로 표시합니다.
        x_start, y_start = x, y  # 클릭한 현재 지점을 드래그의 시작점 좌표로 기록합니다.

    elif event == cv.EVENT_MOUSEMOVE:  # 마우스를 화면 위에서 움직일 때 실행됩니다.
        if is_dragging:  # 마우스 버튼을 누른 채로 움직일 때만 사각형을 그립니다.
            img_display = img_original.copy()  # 이전 사각형 잔상을 지우기 위해 원본을 매번 새로 복사합니다.
            cv.rectangle(img_display, (x_start, y_start), (x, y), (0, 255, 0), 2)  # 실시간 초록색 사각형을 그립니다.

    elif event == cv.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼에서 손을 뗐을 때 실행됩니다.
        is_dragging = False  # 드래그가 끝났으므로 상태를 False로 바꿉니다.
        x_end, y_end = x, y  # 버튼을 뗀 현재 지점을 드래그의 끝점 좌표로 기록합니다.
        
        left, right = min(x_start, x_end), max(x_start, x_end)  # X좌표 중 작은 값을 왼쪽, 큰 값을 오른쪽으로 정합니다.
        top, bottom = min(y_start, y_end), max(y_start, y_end)  # Y좌표 중 작은 값을 위쪽, 큰 값을 아래쪽으로 정합니다.

        if right > left and bottom > top:  # 유의미한 크기의 영역이 선택되었을 경우에만 처리합니다.
            roi = img_original[top:bottom, left:right]  # Numpy 슬라이싱으로 선택 영역 이미지를 잘라냅니다.
            cv.imshow('Selected ROI', roi)  # 잘라낸 이미지(ROI)만 별도의 창으로 즉시 보여줍니다.
            
            img_display = img_original.copy()  # 메인 화면을 다시 깨끗하게 만든 뒤
            cv.rectangle(img_display, (left, top), (right, bottom), (255, 0, 0), 2)  # 선택된 영역을 파란색으로 확정 표시합니다.
        else:  # 클릭만 하고 드래그를 안 했을 경우
            img_display = img_original.copy()  # 화면을 아무것도 없는 깨끗한 원본 상태로 되돌립니다.

# --- 윈도우 창 생성 및 설정 ---
cv.namedWindow('ROI Selection')  # 'ROI Selection'이라는 제목의 빈 윈도우 창을 만듭니다.
cv.setMouseCallback('ROI Selection', on_mouse)  # 해당 창에서 발생하는 마우스 신호를 on_mouse 함수에 연결합니다.

# --- 터미널 안내 문구 출력 ---
print("--- 사용 방법 ---")  # 사용 안내 시작을 알립니다.
print("드래그 : 영역 선택")  # 마우스 조작법을 알려줍니다.
print("r : 영역 선택 리셋 (원본으로)")  # 리셋 기능을 위한 키를 안내합니다.
print("s : 선택 영역 저장 (3_result.jpg)")  # 저장 기능을 위한 키를 안내합니다.
print("q : 종료")  # 종료 기능을 위한 키를 안내합니다.

# --- 메인 루프 (실시간 화면 갱신) ---
while True:  # 사용자가 q를 눌러 종료하기 전까지 계속 돕니다.
    cv.imshow('ROI Selection', img_display)  # 현재 작업 중인 이미지(img_display)를 창에 실시간으로 띄웁니다.
    
    key = cv.waitKey(1) & 0xFF  # 키보드 입력을 1밀리초 동안 기다립니다.

    if key == ord('q'):  # 만약 'q' 키를 눌렀다면
        break  # 무한 루프를 탈출하여 프로그램을 종료 단계로 보냅니다.
    
    elif key == ord('r'):  # 만약 'r' 키를 눌렀다면
        img_display = img_original.copy()  # 화면을 사각형 없는 깨끗한 원본으로 초기화합니다.
        roi = None  # 저장되어 있던 관심 영역(ROI) 데이터를 지웁니다.
        if cv.getWindowProperty('Selected ROI', cv.WND_PROP_VISIBLE) >= 1:  # 잘라낸 창이 열려 있다면
            cv.destroyWindow('Selected ROI')  # 그 창을 닫아버립니다.
        print("화면이 초기화되었습니다.")  # 초기화되었음을 알려줍니다.

    elif key == ord('s'):  # 만약 's' 키를 눌렀다면
        if roi is not None:  # 마우스로 선택해둔 영역(ROI)이 존재할 때만 실행합니다.
            save_path = r'c:\opencv_\computer-vision\opencv\images\3_result.jpg'  # 저장할 파일 경로입니다.
            cv.imwrite(save_path, roi)  # 잘라낸 영역 데이터를 실제 이미지 파일로 저장합니다.
            print(f"이미지가 저장되었습니다: {save_path}")  # 저장 성공 메시지를 출력합니다.
        else:  # 선택한 영역이 없는데 저장을 시도했을 경우
            print("저장할 ROI가 없습니다. 먼저 영역을 선택하세요.")  # 경고 메시지를 출력합니다.

# --- 프로그램 종료 ---
cv.destroyAllWindows()  # 모든 창을 닫고 자원을 해제합니다.
