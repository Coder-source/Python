import cv2 #Use the functions of OpenCV
import numpy

img = numpy.zeros((500, 500, 3), numpy.uint8)
img[:,:] = [255, 255, 255]
cv2.rectangle(img, (200, 50), (300, 150), (0, 0, 200), 3, 4)
cv2.imshow("View Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
