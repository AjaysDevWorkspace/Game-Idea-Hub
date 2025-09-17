import cv2
import numpy as np
import os


lower_color = np.array([94, 80, 2])   
upper_color = np.array([126, 255, 255]) 

cap = cv2.VideoCapture(0)
initial_y = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)

        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 0, 0), 2) 

            if initial_y is None:
                initial_y = y

            if y < initial_y - 40:  
                os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 5)'")
                initial_y = y
            elif y > initial_y + 40:
                os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 5)'")
                initial_y = y

    cv2.imshow("Mac Volume Control (Blue Marker)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
