import time
from utils import distance
from mouse_control import (
    left_click, right_click,
    mouse_down, mouse_up, scroll
)

# ===== Config =====
SCROLL_SENSITIVITY = 400

# ===== States =====
state = "IDLE"
dragging = False
scroll_start_time = 0
prev_index_y = None
last_click = 0

def handle_right_hand(lm):
    global state, dragging, scroll_start_time, prev_index_y, last_click

    thumb = lm[4]
    index = lm[8]
    middle = lm[12]
    ring = lm[16]
    pinky = lm[20]

    now = time.time()

    d_index_thumb = distance(index, thumb)
    d_middle_thumb = distance(middle, thumb)
    d_index_middle = distance(index, middle)

    d_fist = (
        distance(thumb, index) +
        distance(index, middle) +
        distance(middle, ring) +
        distance(ring, pinky)
    )

    # ========= DRAG =========
    if d_fist < 0.35 and not dragging:
        mouse_down()
        dragging = True
        state = "DRAG"

    elif d_fist > 0.6 and dragging:
        mouse_up()
        dragging = False
        state = "IDLE"

    if state == "DRAG":
        return

    # ========= CLICK =========
    if d_index_thumb < 0.04 and now - last_click > 0.6:
        left_click()
        last_click = now

    elif d_middle_thumb < 0.04 and now - last_click > 0.6:
        right_click()
        last_click = now

    # ========= SCROLL =========
    fingers_for_scroll = d_index_middle < 0.05

    if fingers_for_scroll:
        if scroll_start_time == 0:
            scroll_start_time = now
        elif now - scroll_start_time > 0.3:
            state = "SCROLL"
    else:
        scroll_start_time = 0
        state = "IDLE"
        prev_index_y = None

    if state == "SCROLL":
        if prev_index_y is not None:
            dy = index.y - prev_index_y
            scroll_amount = int(-dy * SCROLL_SENSITIVITY)
            if abs(scroll_amount) > 5:
                scroll(scroll_amount)

        prev_index_y = index.y
