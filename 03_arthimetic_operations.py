import cv2 as cv
img1 = cv.imread("sample-img/dog1.jpg", 1)
img2 = cv.imread("sample-img/owl-eyes.jpg", 1)

add_img = cv.add(img1, img2)

cv.imshow("Added", add_img)
cv.waitKey(0)
cv.destroyWindow("Added")

substract_img = cv.subtract(img1, img2)
cv.imshow("Substracted", substract_img)
cv.waitKey(0)

multiply_img = cv.multiply(img1, img2)
cv.imshow("Multiplied", multiply_img)
cv.waitKey(0)

divide_img = cv.divide(img1, img2)
cv.imshow("Divided", divide_img)
cv.waitKey(0)

cv.destroyAllWindows()