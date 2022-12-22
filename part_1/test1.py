import cv2
import numpy as np

face_detector = cv2.CascadeClassifier('part_1\haarcascade_frontalface_default.xml')
#eyes_detector = cv2.CascadeClassifier('part_1\haarcascade_eye.xml')
#lips_detector = cv2.CascadeClassifier('part_1\haarcascade_smile.xml')
    

videoCap = cv2.VideoCapture(0)

while True:
    ret, frame = videoCap.read()
    if ret == False:
        break
    
    effect = cv2.waitKey(100)
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
           
    if effect == 53: #press 5
        faces = face_detector.detectMultiScale(gray_frame, 1.3)
        for x,y,w,h in faces :
            target_frame = gray_frame[y:y+h , x:x+w]
            target_frame_size = w , h
            gray_frame[y:y+h , x:x+w] = cv2.blur(target_frame, target_frame_size)       
    
    elif effect == 27: #esc
       break        
       
    cv2.imshow('output', gray_frame)
    