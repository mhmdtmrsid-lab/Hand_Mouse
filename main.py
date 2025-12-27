import cv2
from camera import init_camera, read_frame
from hand_tracking import process_frame, mp_draw, mp_hands
from mouse_control import move_mouse, screen_w, screen_h
from gestures import handle_right_hand
from utils import map_range

smooth = 5
margin = 0.15
prev_x, prev_y = 0, 0

cap = init_camera()

while True:
    frame = read_frame(cap)
    if frame is None:
        break

    result = process_frame(frame)

    if result.multi_hand_landmarks and result.multi_handedness:
        for i, hand in enumerate(result.multi_hand_landmarks):
            label = result.multi_handedness[i].classification[0].label
            lm = hand.landmark

            index = lm[8]

            # ===== Left Hand (Mouse Move) =====
            if label == "Left":
                x_norm = max(margin, min(1 - margin, index.x))
                y_norm = max(margin, min(1 - margin, index.y))

                x = map_range(x_norm, margin, 1 - margin, 0, screen_w)
                y = map_range(y_norm, margin, 1 - margin, 0, screen_h)

                curr_x = prev_x + (x - prev_x) / smooth
                curr_y = prev_y + (y - prev_y) / smooth

                move_mouse(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

            # ===== Right Hand (Gestures) =====
            if label == "Right":
                handle_right_hand(lm)

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Two-Hand Smart Mouse (Stable)", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
