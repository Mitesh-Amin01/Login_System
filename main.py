import cv2

cap  = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)


imgBackground = cv2.imread('img/bg.jpg')

while True:
    success,img = cap.read()
    
    imgBackground[162:162+480 ,55:55+640] =img
    
    cv2.imshow('Faces Attendance',imgBackground)
    cv2.waitKey(1)