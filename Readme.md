# Handwritten Number Reader

## Introduction

Handwritten Number Reader is a program that lets machine learning to learn the pattern of human handwritten numbers from MNIST dataset included in the Tensorflow library and then use OpenCV and MSS to receive input from the user to recognize the numbers provided by the user. 

## Using it

It was built on Python 3.8, so it is unknown that another version of Python could run this code.

The packages requires to run :
- tensorflow (2.10 or below)
- mss 
- opencv
- numpy

To use it, run it and let the machine learning to do the learning, it will take some times depending on the cpu or gpu performance (depends on which device tensorflow on but it is recommend to run on gpu as it is faster).

After the machine learning has completed its learning, an application will appear that shows a screenshot of a desktop. Now open a paint or any equavalent app that can be drawn onto, and align paint to the screenshot of a desktop. After that, put a black background on the paint and enjoy draw any number with a white colour. Press q to quit the program.

The position of the screenshot can adjust by changing the value of top, left, length and height in the code.

## Note to take about this project

- The machine learning is not optimized so the accuracy of the machine learning output may vary.  However the accuracy of the machine learning is increasing if the numbers is drawn on the center of the screenshot.
- Due to recent update of tensorflow, some commands are depricated. Newer version on tensorflow will not run this code. (will update this issue later) However the code can be run on tensorflow 2.10 or below. 


