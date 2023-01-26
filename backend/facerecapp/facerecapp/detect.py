import cv2
face_cascade = cv2.CascadeClassifier('face_detector.xml')

img = cv2.imread('image.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)


