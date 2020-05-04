import cv2
import numpy as np
import json

path = '../custom_models/ibug_300W_large_face_landmark_dataset/helen/trainset/2418314368_1.jpg'
box = 544, 687, 642, 643
scale_factor = 2

t, l, w, h = [int(np.ceil(i/scale_factor)) for i in box]

image = cv2.imread(path)
image = cv2.resize(image, (0, 0), fx=1/scale_factor, fy=1/scale_factor)

# nl = 0
# nt = 0

# while(True):
#     image_copy = image.copy()
#     cv2.rectangle(image_copy, (nl, nt), (nl+w, nt+h), (0, 0, 200), 2)
#     cv2.imshow('Face', image_copy)
#     nl += 2
#     if nl+w >= image_copy.shape[1]:
#         nl = 0
#         nt += 2

#     if nt in [t-1, t, t+1] and nl in [l-1, l, l+1]:
#         cv2.rectangle(image, (nl, nt), (nl+w, nt+h), (0, 200, 0), 2)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

face_images = json.load(open("images_files.json"))

def get_images():
    cropped_images =[]
    for idx, face_image in enumerate(face_images[0:10]):
        image = cv2.imread('../custom_models/ibug_300W_large_face_landmark_dataset/' + face_image['file'])
        t = face_image['t']
        l = face_image['l']
        w = face_image['w']
        h = face_image['h']
        cropped_image = image[t:t+h, l:l+w]
        cropped_image = cv2.resize(cropped_image, (50, 50))
        cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        cropped_images.append(cropped_image)
        # print(cropped_image)
    return cropped_images

def get_images2():
    cropped_images =[]
    for idx, face_image in enumerate(face_images[10:15]):
        image = cv2.imread('../custom_models/ibug_300W_large_face_landmark_dataset/' + face_image['file'])
        t = face_image['t']
        l = face_image['l']
        w = face_image['w']
        h = face_image['h']
        cropped_image = image[t:t+h, l:l+w]
        cropped_image = cv2.resize(cropped_image, (50, 50))
        cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        cropped_images.append(cropped_image)
        # print(cropped_image)
        # cv2.imshow("image", cropped_image)
        # cv2.waitKey(0)
    return cropped_images

def get_images3():
    cropped_images =[]
    for idx, face_image in enumerate(face_images[10:20]):
        image = cv2.imread('../custom_models/ibug_300W_large_face_landmark_dataset/' + face_image['file'])
        t = face_image['t']
        l = face_image['l']
        w = face_image['w']
        h = face_image['h']
        cropped_image = image[0:20, 0:20]
        cropped_image = cv2.resize(cropped_image, (50, 50))
        cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        cropped_images.append(cropped_image)
        # print(cropped_image)
        # cv2.imshow("image", cropped_image)
        # cv2.waitKey(0)
    return cropped_images

get_images2()
cv2.destroyAllWindows()