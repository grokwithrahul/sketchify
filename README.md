# Sketchify

A simple sketching software to convert an image to a realistic sketch!

Installation
------------
    pip install sketchify

#### Installation notes
sketchify depends on `opencv-contrib-python`.

## Usage

    from sketchify import sketch
    img = sketch.normalsketch(‘path/to/image.extension’, 'path/to/save/image', 'saveimagename')

## Examples
Go to tests/test_images for more examples.

Obama Original|Obama Sketchified
:-------------------------------------------------------:|:--------------------------------------------------------------:
![Obama Original](tests/test_images/original/normalsketch/image1.jpg) |  ![Obama Sketchified](tests/test_images/sketchified/normalsketch/image1.png)

Colloseum Original|Colloseum Sketchified
:-----------------------------------------------------------:|:------------------------------------------------------------------:
![Colloseum Original](tests/test_images/original/normalsketch/image2.jpg)| ![Colloseum SKetchified](tests/test_images/sketchified/normalsketch/image2.png)

## Article
https://medium.com/analytics-vidhya/image-to-pencil-sketch-in-just-2-lines-of-code-292de57be483