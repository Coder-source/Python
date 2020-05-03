import cv2 #Use the functions of OpenCV
import numpy

img = numpy.zeros((500, 500, 3), numpy.uint8)
cv2.circle(img, (250, 250), 200, (0, 200, 255))
cv2.imshow("View Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
