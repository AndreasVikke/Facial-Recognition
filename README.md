# Facial-Recognition

### Authors
Andreas Zoega Vikke
https://andreasvikke.dk/

Martin Eli Frederiksen
https://github.com/MartinFrederiksen

### Description
This project is a Facial Recognition libary which can be imported into other programs or run standalone form the Command-line.

It's created in Python and is run with the use of OpenCV and dlib

### Important external uses
|Libary|Version|
|---|---|
|[dlib](https://pypi.org/project/dlib/)|19.19.0|
|[opencv-python](https://pypi.org/project/opencv-python/)|4.2.0.34|

|Model|
|---|
|[dlib_face_recognition_resnet_model_v1](https://github.com/davisking/dlib-models)|
|[shape_predictor_68_face_landmarks](https://github.com/davisking/dlib-models)|

### Stand-alone use (command-line interface)
![CLI Help](https://raw.githubusercontent.com/AndreasVikke/Facial-Recognition/master/images/readme/Console-Help.png)

You can use this libary standalone in the command-line:
``` 
$ python FacialRecognition.py PATH
```
Replace **PATH** with an image or video path.
**PATH** can also be an integer corresponding to an index of a webcam

Press **Q** to close the CLI

### Examples of commands in the stand-alone prompt:
Get webcam output with Facial Recogniton:
```
$ python FacialRecognition.py 1
```
![Webcam output](https://raw.githubusercontent.com/AndreasVikke/Facial-Recognition/master/images/readme/webcam.gif)

Get faces on image with features and tolerance at 0.62:
```
$ python FacialRecognition.py PATH -f=True -t=0.62
```
![Image with features](https://raw.githubusercontent.com/AndreasVikke/Facial-Recognition/master/images/readme/FredVikke.png)