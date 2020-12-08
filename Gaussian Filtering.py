import numpy as np
from PIL import  Image
import cv2
folder_path = "face-2.jpg"
def convolve2d(image, kernel):
    """
    This function which takes an image and a kernel and returns the convolution of them.

    :param image: a numpy array of size [image_height, image_width].
    :param kernel: a numpy array of size [kernel_height, kernel_width].
    :return: a numpy array of size [image_height, image_width] (convolution output).
    """
    # Flip the kernel
    kernel = np.flipud(np.fliplr(kernel))
    # convolution output
    output = np.zeros_like(image)

    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    image_padded[1:-1, 1:-1] = image

    # Loop over every pixel of the image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y, x]=(kernel * image_padded[y: y+3, x: x+3]).sum()

    return output


def GaussianBlurImage(image, sigma):
    # image = imread(image)
    #image = Image.open(image)
    sigma = sigma/10
    image = np.asarray(image)
    # print(image)
    filter_size = 2 * int(4 * sigma + 0.5) + 1
    gaussian_filter = np.zeros((filter_size, filter_size), np.float32)
    m = filter_size // 2
    n = filter_size // 2

    for x in range(-m, m + 1):
        for y in range(-n, n + 1):
            x1 = 2 * np.pi * (sigma ** 2)
            x2 = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
            gaussian_filter[x + m, y + n] = (1 / x1) * x2
            print("a1")

    im_filtered = np.zeros_like(image, dtype=np.float32)
    #for c in range(3):
    im_filtered = convolve2d(image, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16)
    print('returning')
    return (im_filtered.astype(np.uint8))


def normal_sketch(path):
    original_img = cv2.imread(path)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255 - gray_img
    blurred_img = GaussianBlurImage(gray_inverse, 10)
    blurred_inverse = 255 - blurred_img
    output = cv2.divide(gray_img, blurred_inverse, scale=256.0)
    print('cd')
    return output

sketchdeep = normal_sketch(folder_path)
cv2.imwrite('sketchdeep.png', sketchdeep)
print("hellko")
arshdeep_og = cv2.imread('arshdeep singh.jpg')
arshdeep_bw = cv2.cvtColor(arshdeep_og, cv2.COLOR_BGR2GRAY)
arshdeep = GaussianBlurImage(arshdeep_bw, 5)
cv2.imwrite('arshdeep_filtered.png', arshdeep)
