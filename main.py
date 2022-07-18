import cv2
from random import randrange
data = cv2.CascadeClassifier('D:/opencv/R/xml/haarcascade_frontalface_default.xml')
# the source is the webcam
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 3 capture hight
webcam.set(3, 640)
# 4 capture width
webcam.set(4, 480)
# 10 capture brightness
webcam.set(10, 100)
while True:
    success, frame = webcam.read()
    frame = cv2.flip(frame, 99)

    # convert to gray
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = data.detectMultiScale(Gray)
    for (x, y, w, h) in face:
        # randrange(255) will give random color but it will make it slower
        # put rectangle on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, randrange(255)), 2)
        cv2.imshow('frame', frame)
    # Canny filter
    imgcanny = cv2.Canny(frame, 100, 100)
    cv2.imshow('imgcanny', imgcanny)

    # gausiian filter to blur the image
    imgblur = cv2.GaussianBlur(frame, (7,7),0)
    cv2.imshow('imgblur', imgblur)

    # cv2.imshow('frame', frame)
    # wait to click a button to close the program
    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord("q"):
        break
webcam.release()
cv2.destroyAllWindows()
# (x, y) is the upper left corner
# ( x+w, y+h) is the lower right
# (255, 0, 0) is PGR NOT RGB it is backward it is the color of the rectangle
# 2 is the thickness of the rectangle
