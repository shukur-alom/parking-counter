import cv2
import numpy as np

# List to store points
points = []
poligon = []


# Function to draw polygon
def draw_polygon(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))


# Create a black image, a window and bind the function to window
cap = cv2.VideoCapture("Media/3214448-hd_1920_1080_25fps.mp4")
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_polygon)

while 1:
    ret, frame = cap.read()
    if not ret:
        break
    mask = np.zeros_like(frame)
    for i in poligon:
        # Assuming 'frame' is your original image and 'i' is your polygon points
        cv2.fillPoly(mask, [np.array(i)], (124, 255, 112))

    frame = cv2.addWeighted(mask, 0.2, frame, 1, 0)

    for x, y in points:
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow("image", frame)

    wail_key = cv2.waitKey(1)

    if wail_key == ord("s"):
        if len(points) > 0:
            poligon.append(points)
            points = []

    elif wail_key == ord("r"):
        try:
            poligon.pop()
        except:
            pass
    elif wail_key & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
