import cv2
face_cascade = cv2.CascadeClassifier('face_detector.xml')

img = cv2.imread('image.jpg')
