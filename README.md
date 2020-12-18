# Sketchify

A simple sketching software to convert an image to a realistic sketch!

Installation
------------
    pip install sketchify

#### Installation notes
sketchify depends on `opencv-contrib-python`.

## Usage

    from sketchify import sketch
    import cv2
    img = sketch.normalsketch(‘path/to/image.extension’)
    cv2.imsave(‘path.png’, img)

## Examples
Go to tests/test_images for more examples.

Obama Original|Obama Sketchified
:-------------------------------------------------------:|:--------------------------------------------------------------:
![Obama Original](tests/test_images/original/image1.jpg) |  ![Obama Sketchified](tests/test_images/sketchified/image1.png)

Colloseum Original|Colloseum Sketchified
:-----------------------------------------------------------:|:------------------------------------------------------------------:
![Colloseum Original](tests/test_images/original/image2.jpg)| ![Colloseum SKetchified](tests/test_images/sketchified/image2.png)