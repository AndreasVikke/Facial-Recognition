import cv2
import numpy as np
import test_nn4
import json

class Conv2D:
    def __init__(self, outputs):
        self.kernels = np.array([
            [
                [5, 5, 5],
                [-3, -3, -3],
                [-3, -3, -3]
            ],
            [
                [5, -3, -3],
                [5, -3, -3],
                [5, -3, -3]
            ],
            [
                [-1, -2, -1],
                [0, 0, 0],
                [1, 2, 1]
            ]
        ], dtype=np.float32)

    def process(self, img, filters):
        images = []
        # accum = np.zeros_like(img)
        for kern in filters:
            fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
            # fimg = test_nn4.convolution_layer(img, kern)
            # test_nn4.relu_layer(fimg, len(img[0]))
            images.append(fimg)
            # np.maximum(accum, fimg, accum)
        return images

test = Conv2D(32)


face_images = json.load(open("images_files.json"))
face_image = face_images[116]
image = cv2.imread('../custom_models/ibug_300W_large_face_landmark_dataset/' + face_image['file'])
t = face_image['t']
l = face_image['l']
w = face_image['w']
h = face_image['h']
cropped_image = image[t:t+h, l:l+w]
cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
cropped_image = cv2.resize(cropped_image, (200, 200))

p = test.process(cropped_image, test.kernels)

print(len(p))
cv2.imshow("Image", cropped_image)
cv2.waitKey(0)
for i in p:
    print(i)
    cv2.imshow("Image", i)
    cv2.waitKey(0)