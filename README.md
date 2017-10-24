## Installation
**MAC**
1. Install homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
1. Install Python
```
brew install python
```
1. Install OpenCV
```
brew install opencv
```
1. Final setup step
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