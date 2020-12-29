import cv2


def dreamsketch(path):  
    original_img = cv2.imread(path)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255 - gray_img
    blurred_img = cv2.GaussianBlur(gray_inverse, (21, 21), sigmaX=100, sigmaY=100)
    output = cv2.divide(gray_img, blurred_img, scale=256.0)
    return output


def normalsketch(impath, savepath, savename, scale=10):
    if scale > 10 or scale < 1:
        raise ValueError('Errno 1: Scale must be between 1 and 10')
    if not isinstance(scale, int):
        raise TypeError('Errno 2: Scale must be an integer value')
    if not isinstance(impath, str) or not isinstance(savepath, str):
        raise TypeError('Errno 3: Path to image must be a string')
    original_img = cv2.imread(impath)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray_inverse = 255-gray_img
    sigma = scale*1.5
    blurred_img = cv2.GaussianBlur(gray_inverse, (51, 51), sigmaX=sigma, sigmaY=sigma)
    blurred_inverse = 255 - blurred_img
    output = cv2.divide(gray_img, blurred_inverse, scale=256.0)
    cv2.imwrite(f'{savepath}/{savename}.png', output)


def pop(impath, savepath, savename):
    img = cv2.imread(impath)
    edges = cv2.Canny(img, 100, 200, L2gradient=True)
    edge_inv = 255 - edges
    edge_inv = cv2.cvtColor(edge_inv, cv2.COLOR_GRAY2RGB)
    final= cv2.bitwise_and(img, edge_inv)
    cv2.imwrite(f'{savepath}/{savename}.png', final)
