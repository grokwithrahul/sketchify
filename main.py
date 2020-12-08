import cv2

class sketch():
    def __init__(self):
        pass

    def dreamsketch(path):
        original_img = cv2.imread(path)
        gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        gray_inverse = 255 - gray_img
        blurred_img = cv2.GaussianBlur(gray_inverse, (21, 21), sigmaX=100, sigmaY=100)
        output = cv2.divide(gray_img, blurred_img, scale=256.0)
        return output

    def normal_sketch(path):
        original_img = cv2.imread(path)
        gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        gray_inverse = 255-gray_img
        blurred_img = cv2.GaussianBlur(gray_inverse, (51, 51), sigmaX=100, sigmaY=100)
        blurred_inverse = 255 - blurred_img
        output = cv2.divide(gray_img, blurred_inverse, scale=256.0)
        return output
