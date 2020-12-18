from sketchify import sketch
import cv2

path = './tests/test_images/original/image3.png'
image = sketch.normalsketch(path, 1)
cv2.imwrite('./tests/test_images/sketchified/image3.png', image)