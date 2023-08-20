import cv2

video = cv2.VideoCapture('wind-turbines-in-the-sea.mp4')

while True:
    success, img = video.read()
    cv2.imshow('Water', img)

    key = cv2.waitKey(10)

    if key == ord('c'):
        break
