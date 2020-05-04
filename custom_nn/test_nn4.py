from multiprocessing import Pool
import threading
from tqdm import tqdm
import numpy as np
import json
import cv2

path = '../custom_models/ibug_300W_large_face_landmark_dataset/helen/trainset/2652699508_1.jpg'

feature_size = 3
kernel = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

def convolution_layer(image):
    # pool = Pool(8)
    # # convo_image = pool.map(convolute_cords, range(len(image[0]) - 2))
    # convo_image = pool.map(convolute_cords, [(x, image) for x in range(len(image[0]))])
    # pool.close()
    # pool.join()
    convo_image = []
    for x in range(len(image[0])):
        convo_image.append(convolute_cords((x, image)))

    return np.array(relu_layer(convo_image, len(image[0])))

def convolute_cords(args):
    x, image = args
    row = []
    for y in range(len(image[0]) - 2):
        snippet = image[x:x+feature_size, y:y+feature_size]
        multiply = np.array([np.array(a, dtype=np.int16) * np.array(kernel[idx], dtype=np.int16) for idx, a in enumerate(snippet)])
        res = sum(sum(multiply)) / len(image[0])
        row.append(res)
    return row

def relu_layer(image, width):
    relu_image = []
    for x in range(width - 2):
        row = []
        for y in range(width - 2):
            row.append(_relu(image[y][x]))
        relu_image.append(row)
    # return relu_image
    return pooling_layer(relu_image, len(relu_image[0]))

def _relu(n):
    if n < 0:
        return 0
    return n

def pooling_layer(image, width):
    pooling_image = []
    for x in range(int(np.ceil(width/2))):
        X = x * 2
        row = []
        for y in range(int(np.ceil(width/2))):
            Y = y * 2
            row.append(pooling(np.array([*image[Y][X:X+2], *image[Y + (1 if Y != width-1 else 0)][X:X+2]])))
        pooling_image.append(row)
    return pooling_image

def pooling(numbers):
    return numbers.max()


image = cv2.imread(path)
image = image[346:346+841, 665:665+833]
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (200, 200))

face_images = json.load(open("images_files.json"))

def get_images(n):
    face_image = face_images[n]
    image = cv2.imread('../custom_models/ibug_300W_large_face_landmark_dataset/' + face_image['file'])
    t = face_image['t']
    l = face_image['l']
    w = face_image['w']
    h = face_image['h']

    cropped_image = image[t:t+h, l:l+w]
    cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    cropped_image = cv2.resize(cropped_image, (200, 200))

    return convolution_layer(convolution_layer(cropped_image))

def test():
    pool = Pool(8)
    images = list(tqdm(pool.imap(get_images, range(50)), total=50))
    pool.close()
    pool.join()

    print([len(image) for image in images])

test()
