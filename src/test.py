import numpy as np
import itertools
import cv2
import os
from table import Table

cap = cv2.VideoCapture('video_samples/long_sample.mp4')

'''
    Calibration switch (debugging only)
'''
#Uncalibrated
#table = Table()
#Calibrated

#Data path
data_path = "%s/poolcampro/data/table_calibration/" % \
            (os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

table = Table(np.load(data_path+'corners.npy'), np.load(data_path+'boundaries.npy'), True)

while cap.isOpened():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    if not table.is_calibrated():
        #Pre-processing
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        gray = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150, 200, 14, 15)
        table.calibrate_table(circles)
    circles, shape = table.get_table_details()
    x, y, w, h=cv2.boundingRect(shape)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 1)
        # draw the center of the circle
        cv2.circle(frame,(i[0], i[1]), 2, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        table.calibrated(True)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
