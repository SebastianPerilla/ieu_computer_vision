import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow('frame', frame)

    c = cv2.waitKey(1)
    
    if c == ord('a'):
        cv2.imwrite('img.jpg', frame)
    if c == 27:  # ESC key
        break
    
cap.release()
cv2.destroyAllWindows()