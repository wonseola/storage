import cv2
import numpy as np
import random

window_name = 'click click ~~'
window_width, window_height, score = 800, 600, 0

def create_circle(): # 동그라미 나오기 크기, 위치 랜덤!
    global circle_radius
    circle_radius = random.randrange(8, 30)
    x = random.randint(circle_radius, window_width - circle_radius)
    y = random.randint(circle_radius, window_height - circle_radius)
    return (x, y)

def update_circle(): # 클릭하면 다른위치로, 색도 바꾸기
    global circle_position, circle_color
    circle_position = create_circle()
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def mouse_click(event, x, y, flags, param):
    global score
    if event == cv2.EVENT_LBUTTONDOWN:
        # 원 중심
        distance = np.sqrt((x - circle_position[0]) ** 2 + (y - circle_position[1]) ** 2)
        if distance <= circle_radius: #클릭하면 점수 +, 새로운 동그라미
            score += 1
            update_circle()

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_click)

# 처음 위치, 색 설정
circle_position = create_circle()
circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
while True:
    frame = np.full((window_height, window_width, 3), (255, 204, 204), dtype=np.uint8)  
    cv2.circle(frame, circle_position, circle_radius, circle_color, -1)
    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    cv2.imshow(window_name, frame)
    
    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.destroyAllWindows()
