import cv2
import mediapipe as mp
import random

window_name = 'click click ~~'
window_width, window_height, score = 800, 600, 0

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def create_circle():
    global circle_radius
    circle_radius = random.randrange(8, 30)
    x = random.randint(circle_radius, window_width - circle_radius)
    y = random.randint(circle_radius, window_height - circle_radius)
    return (x, y)

def update_circle():
    global circle_position, circle_color
    circle_position = create_circle()
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def mouse_click(x, y):
    global score
    distance = ((x - circle_position[0]) ** 2 + (y - circle_position[1]) ** 2) ** 0.5
    if distance <= circle_radius:
        score += 1
        update_circle()

cv2.namedWindow(window_name)

circle_position = create_circle()
circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (window_width, window_height))
    
    # 손 모양 감지
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger_tip.x * window_width), int(index_finger_tip.y * window_height)
            cv2.circle(frame, (x, y), 10, (130, 0, 130), -1)
            mouse_click(x, y)
    
    cv2.circle(frame, circle_position, circle_radius, circle_color, -1)
    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    cv2.imshow(window_name, frame)
    
    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
