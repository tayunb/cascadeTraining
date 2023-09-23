import cv2
import time

cap = cv2.VideoCapture('teste_videos/robocup3.avi')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ball_cascade = cv2.CascadeClassifier('cascade_files/cascade.xml')

    if(ball_cascade.empty()):
        raise Exception
    
    ball = ball_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(10,10))

    for (x, y, w, h) in ball:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)


    cv2.imshow('teste', frame)
    cv2.waitKey(30)