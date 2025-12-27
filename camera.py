import cv2

def init_camera():
    return cv2.VideoCapture(0)

def read_frame(cap):
    success, frame = cap.read()
    if not success:
        return None
    return cv2.flip(frame, 1)
