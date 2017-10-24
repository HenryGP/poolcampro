## Usage

Execute _poolcampro.py_ to start the program execution. 

```
$ src/poolcampro.py -h
usage: poolcampro.py [-h] [-f FILE] [-c] [-v] mode

positional arguments:
  mode                  live|file

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  absolute path to video file to stream from
  -c, --calibrate       start the program for calibration of the table
  -v, --verbose         increase output verbosity
```

The `mode` is mandatory and defines whether:
- To read data from a video file. This requires the -f parameter to specify the location of the video file OR
- To read data from a videocamara.

Initially, for calibrating the Table boundaries, the program requires to start with the `--calibrate` option paramter. Press the 'c' button on the keyboard to record the current pocket coordinates, this will be stored under */data/table_calibration* and used to crop the table when executing the program without the `--calibrate` parameter. 

## Installation
**MAC**
1. Install homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python
```
brew install python
```
3. Install OpenCV
```
brew install opencv
```
4. Final setup step
```
brew info opencv
```
Instructions will be provided at the bottom of the output with the required changes to be able to import OpenCV into your Python program.
In my case, they were the following:
```
==> Caveats
Python modules have been installed and Homebrew's site-packages is not
in your Python sys.path, so you will not be able to import the modules
this formula installed. If you plan to develop with these modules,
please run:
  mkdir -p /Users/egarnelo/Library/Python/2.7/lib/python/site-packages
  echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/egarnelo/Library/Python/2.7/lib/python/site-packages/homebrew.pth
```
