#!/usr/bin/python

import argparse
import sys
import numpy as np
import itertools
import cv2
import os
from table import Table

def capture_video(file_path, calibration):
    cap = cv2.VideoCapture(file_path)

    if calibration:
        table = Table()       
    else:
        #Calibrated data path
        data_path = "%s/data/table_calibration/" % \
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
        if calibration and not table.is_calibrated(): #Draw rectangle and circles with the whole video if calibrating
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 1)
                # draw the center of the circle
                cv2.circle(frame,(i[0], i[1]), 2, (0, 0, 255), 2)
            cv2.imshow('frame', frame)
        else:
            #cropped_frame = frame[200:400, 100:300] # Crop from x, y, w, h -> 100, 200, 300, 400
            cropped_frame = frame[y:y+h,x:x+w]
            # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
            cv2.imshow("cropped", cropped_frame)


        if cv2.waitKey(1) & 0xFF == ord('c'):
            table.calibrated(True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="live|file")
parser.add_argument("-f","--file", help="absolute path to video file to stream from")
parser.add_argument("-c","--calibrate", help="start the program for calibration of the table",action='store_true')
parser.add_argument("-v", "--verbose", help="increase output verbosity",action='store_true')
args = parser.parse_args()
verbose = args.verbose
calibration = args.calibrate
if args.mode=='live':
    print "This mode is not implemented yet"
    sys.exit()
else: #Read from file
    video_file = args.file
print calibration
capture_video(args.file, calibration)
