# Facial-Recognition

### Author
Andreas Zoega Vikke
https://andreasvikke.dk/

### Description
This project is for home automation with IKEA Trådfri Gateway. It's created to be used on a 7" Raspberry PI screen, which is located in the foyer.

It's created in Python and is run with a flask server.

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
```python 
$ python FacialRecognition.py PATH
```
Replace **PATH** with an image or video path.
**PATH** can also be an integer corresponding to an index of a webcam

Press **Q** to close the CLI

### Examples of commands in the stand-alone prompt:
Get webcam output with Facial Recogniton:
```python
$ python FacialRecognition.py 1
```
![Webcam output](https://raw.githubusercontent.com/AndreasVikke/Facial-Recognition/master/images/readme/webcam.gif)

Get faces on image with features and tolerance at 0.62:
```python
$ python FacialRecognition.py PATH -f=True -t=0.62
```
![Image with features](https://raw.githubusercontent.com/AndreasVikke/Facial-Recognition/master/images/readme/FredVikke.png)