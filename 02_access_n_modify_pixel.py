import cv2

img = cv2.imread("sample-img/kurt.jpg")
px = img[100,100]
# B G R
print(px)
print(img.shape)
print(img.dtype)
