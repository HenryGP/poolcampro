#!/usr/bin/python

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("mode", help="live|file")
parser.add_argument("-f","--file", help="absolute path to video file to stream from")
parser.add_argument("-c","--calibrate", help="start the program for calibration of the table",action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
args = parser.parse_args()

verbose = args.verbose
calibration = False

if args.mode=='live':
    print "This mode is not implemented yet"
    sys.exit()
else:
    try:
        video_file = args.file
    except expression as identifier:
        pass

if args.calibrate==True:
    video_file = args.file
    calibration = args.calibrate


print "Calibration", str(calibration)
print "Video file", str(video_file)
print "Verbose", str(verbose)
