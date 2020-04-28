import FacialRecognitionData as frld
import numpy as np
import argparse
import sys
import cv2
import os

camera = 2

cap = cv2.VideoCapture(camera)

process_frame = True
draw_features = True

while(True):
    ret, frame = cap.read()

    face_locations = frld.face_location_data(frame)
    landmarks = frld._faces_landmarks_data_eyes(frame, face_locations)
    landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]
    for points in landmarks_as_tuples:
        for point in points:
            cv2.circle(frame, point, 2, (0,255,0), -1)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()