import numpy as np
import cv2

img = cv2.imread("sample-img/kurt.jpg", 1)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imwrite("sample-img/cobain.png", img)
cv2.destroyAllWindows()
