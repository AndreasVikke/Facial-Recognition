import numpy as np
import cv2

_min_face_size = 20
_scale_factor = 0.709

def __scale_image(image, scale: float):
        height, width, _ = image.shape

        width_scaled = int(np.ceil(width * scale))
        height_scaled = int(np.ceil(height * scale))

        im_data = cv2.resize(image, (width_scaled, height_scaled))

        # Normalize the image's pixels
        im_data_normalized = (im_data - 127.5) * 0.0078125

        return im_data_normalized

def __compute_scale_pyramid(m, min_layer):
        scales = []
        factor_count = 0

        while min_layer >= 12:
            scales += [m * np.power(_scale_factor, factor_count)]
            min_layer = min_layer * _scale_factor
            factor_count += 1

        return scales

image = cv2.imread("../images/train/Vikke.jpg")
height, width, _ = image.shape

m = 12 / _min_face_size
min_layer = np.amin([height, width]) * m

scales = __compute_scale_pyramid(m, min_layer)

cv2.imshow("Original Scale", image)

for scale in scales:
    scaled_image = __scale_image(image, scale)
    cv2.imshow(str(scale), ((scaled_image+1)*255/2).astype('uint8'))

    # Adds a dimention to the image array
    img_x = np.expand_dims(scaled_image, 0)
    # Transposes the img x array permutet by (0, 2, 1, 3)
    img_y = np.transpose(img_x, (0, 2, 1, 3))
    print(img_y)


cv2.waitKey(0)
cv2.destroyAllWindows()