import numpy
import argparse
import cv2

image = cv2.imread('/home/yuejingzhe/Downloads/test.jpg')
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)


    #[x,y] is the kernel for bluring
    #the large kernel becomes, the more blurred imag will appear
    #hstack is able to stack multiple images together
    #using simple mean to average
blurred = numpy.hstack([
cv2.blur(gray, (3,3)),
cv2.blur(gray, (5,5)),
cv2.blur(gray, (7,7))])

    #display two images in a figure
cv2.imshow("Blurring by average", blurred)

cv2.imwrite("1_blur_by_average.jpg", blurred)


if(cv2.waitKey(0)==27):
    cv2.destroyAllWindows()