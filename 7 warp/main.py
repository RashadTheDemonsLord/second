import numpy as np
import math as m
import cv2
import numpy

# to find the coordinate  of point we need to creat a function to call it when using cv2.setMouseCallback
# event is moving the mouse if not mentioned
def printcoo (event, x , y , flag, params ):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x, ',', y)

img = cv2.imread('D:/opencv/R/img/w1.jpg')
print(img.shape)
img = cv2.resize(img, (303, 402))
cv2.imshow('original', img)

#w = m.dist([118 , 62], [266 , 77])
#w = m.ceil(w)
#h = m.dist([266 , 77], [73 , 365])
#h = m.ceil(h)
#print("w is",w,"\n","h is ",h)

# setMouseCallback take 2 argument, the name of the window, and the function that print (printcoo)
cv2.setMouseCallback("original", printcoo )
w, h= 235, 400
pts1 = np.float32([ [118 , 62], [266 , 77], [73 , 365], [224 , 392]])
pts2 = np.float32([[0, 0], [w,0],[0, h], [w, h]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgoutput = cv2.warpPerspective(img,matrix, (w, h))
cv2.imshow('imgoutput', imgoutput)

imgoutput = cv2.warpPerspective(img,matrix, (w, h))
cv2.imshow('imgoutput2', imgoutput)
cv2.waitKey()