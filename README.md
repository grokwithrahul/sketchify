# Sketchify

A simple sketching software to convert an image to a realistic sketch!

from sketchify import sketch
import cv2
img = sketch.normalsketch(‘path/to/image.extension’)
cv2.imsave(‘path.png’, img)

![Obama original]